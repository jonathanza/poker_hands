"""
Tests for the FastAPI REST API.
"""

import unittest

from fastapi.testclient import TestClient

from api.main import app


class TestHealthEndpoint(unittest.TestCase):
    """Test cases for health check endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = TestClient(app)

    def test_health_check(self):
        """Test health check endpoint returns correct status."""
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["version"], "3.0.0")


class TestClassifyEndpoint(unittest.TestCase):
    """Test cases for classify endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = TestClient(app)

    def test_classify_royal_flush(self):
        """Test classifying a royal flush."""
        payload = {
            "cards": [("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")]
        }

        response = self.client.post("/api/v1/classify", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["hand_type"], "Royal Flush")
        self.assertEqual(data["strength"], 10)
        self.assertEqual(len(data["cards"]), 5)

    def test_classify_straight_flush(self):
        """Test classifying a straight flush."""
        payload = {
            "cards": [("9", "S"), ("8", "S"), ("7", "S"), ("6", "S"), ("5", "S")]
        }

        response = self.client.post("/api/v1/classify", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["hand_type"], "Straight Flush")
        self.assertEqual(data["strength"], 9)

    def test_classify_high_card(self):
        """Test classifying high card."""
        payload = {
            "cards": [("A", "H"), ("K", "D"), ("Q", "C"), ("J", "S"), ("9", "H")]
        }

        response = self.client.post("/api/v1/classify", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["hand_type"], "High Card")
        self.assertEqual(data["strength"], 1)

    def test_classify_invalid_cards_count(self):
        """Test that invalid card count is rejected."""
        payload = {"cards": [("A", "H"), ("K", "H"), ("Q", "H")]}  # Only 3 cards

        response = self.client.post("/api/v1/classify", json=payload)

        self.assertEqual(response.status_code, 422)

    def test_classify_duplicate_cards(self):
        """Test that duplicate cards are rejected."""
        payload = {
            "cards": [
                ("A", "H"),
                ("A", "H"),  # Duplicate
                ("K", "H"),
                ("Q", "H"),
                ("J", "H"),
            ]
        }

        response = self.client.post("/api/v1/classify", json=payload)

        self.assertEqual(response.status_code, 422)

    def test_classify_invalid_rank(self):
        """Test that invalid rank is rejected."""
        payload = {
            "cards": [("X", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")]
        }

        response = self.client.post("/api/v1/classify", json=payload)

        self.assertEqual(response.status_code, 422)


class TestBatchClassifyEndpoint(unittest.TestCase):
    """Test cases for batch classify endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = TestClient(app)

    def test_batch_classify_multiple_hands(self):
        """Test classifying multiple hands in batch."""
        payload = [
            {"cards": [("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")]},
            {"cards": [("2", "S"), ("3", "S"), ("4", "S"), ("5", "S"), ("6", "S")]},
            {"cards": [("A", "H"), ("K", "D"), ("Q", "C"), ("J", "S"), ("9", "H")]},
        ]

        response = self.client.post("/api/v1/classify/batch", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]["hand_type"], "Royal Flush")
        self.assertEqual(data[1]["hand_type"], "Straight Flush")
        self.assertEqual(data[2]["hand_type"], "High Card")

    def test_batch_classify_empty_list(self):
        """Test that empty batch is rejected."""
        response = self.client.post("/api/v1/classify/batch", json=[])

        self.assertEqual(response.status_code, 400)

    def test_batch_classify_too_many_hands(self):
        """Test that batches over 100 are rejected."""
        payload = [
            {"cards": [("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")]}
        ] * 101

        response = self.client.post("/api/v1/classify/batch", json=payload)

        self.assertEqual(response.status_code, 400)


class TestCompareEndpoint(unittest.TestCase):
    """Test cases for compare endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = TestClient(app)

    def test_compare_hands_hand1_wins(self):
        """Test comparing hands where hand1 wins."""
        payload = {
            "hand1": [("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")],
            "hand2": [("2", "S"), ("3", "D"), ("4", "C"), ("5", "H"), ("7", "S")],
        }

        response = self.client.post("/api/v1/compare", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["winner"], "hand1")
        self.assertEqual(data["hand1"]["hand_type"], "Royal Flush")
        self.assertEqual(data["hand2"]["hand_type"], "High Card")

    def test_compare_hands_hand2_wins(self):
        """Test comparing hands where hand2 wins."""
        payload = {
            "hand1": [("2", "S"), ("3", "D"), ("4", "C"), ("5", "H"), ("7", "S")],
            "hand2": [("A", "H"), ("A", "D"), ("K", "C"), ("K", "S"), ("Q", "H")],
        }

        response = self.client.post("/api/v1/compare", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["winner"], "hand2")
        self.assertEqual(data["hand1"]["hand_type"], "High Card")
        self.assertEqual(data["hand2"]["hand_type"], "Two Pair")

    def test_compare_hands_tie(self):
        """Test comparing hands that tie."""
        payload = {
            "hand1": [("A", "H"), ("K", "D"), ("Q", "C"), ("J", "S"), ("9", "H")],
            "hand2": [("A", "S"), ("K", "C"), ("Q", "H"), ("J", "D"), ("8", "S")],
        }

        response = self.client.post("/api/v1/compare", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["winner"], "tie")
        self.assertEqual(data["hand1"]["hand_type"], "High Card")
        self.assertEqual(data["hand2"]["hand_type"], "High Card")


class TestRootEndpoint(unittest.TestCase):
    """Test cases for root endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = TestClient(app)

    def test_root_redirects_to_docs(self):
        """Test that root redirects to API docs."""
        response = self.client.get("/", follow_redirects=False)

        self.assertEqual(response.status_code, 307)
        self.assertEqual(response.headers["location"], "/api/docs")


if __name__ == "__main__":
    unittest.main()
