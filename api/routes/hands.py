"""
Poker hand classification endpoints.
"""

from typing import List

from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError

from api.schemas import ClassifyRequest, ClassifyResponse, CompareRequest, CompareResponse
from core import Card, Hand, HandClassifier

router = APIRouter(prefix="/api/v1", tags=["hands"])


@router.post(
    "/classify",
    response_model=ClassifyResponse,
    status_code=status.HTTP_200_OK,
    summary="Classify a Poker Hand",
    description="Classify a single 5-card poker hand and return its type and strength",
)
async def classify_hand(request: ClassifyRequest) -> ClassifyResponse:
    """
    Classify a poker hand.

    Args:
        request: ClassifyRequest with 5 cards

    Returns:
        ClassifyResponse with hand type, strength, and formatted cards

    Raises:
        HTTPException: If validation fails or cards are invalid
    """
    try:
        # Create Hand from request
        cards = [Card(rank=r, suit=s) for r, s in request.cards]
        hand = Hand(cards=cards)

        # Classify
        hand_type = HandClassifier.classify(hand)

        # Format cards for response
        formatted_cards = [str(card) for card in hand.cards]

        return ClassifyResponse(
            hand_type=str(hand_type),
            strength=hand_type.value,
            cards=formatted_cards,
        )

    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid hand: {str(e)}",
        ) from e
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e


@router.post(
    "/classify/batch",
    response_model=List[ClassifyResponse],
    status_code=status.HTTP_200_OK,
    summary="Classify Multiple Poker Hands",
    description="Classify multiple poker hands in a single request",
)
async def classify_batch(requests: List[ClassifyRequest]) -> List[ClassifyResponse]:
    """
    Classify multiple poker hands.

    Args:
        requests: List of ClassifyRequest objects

    Returns:
        List of ClassifyResponse objects

    Raises:
        HTTPException: If any validation fails
    """
    if not requests:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one hand required",
        )

    if len(requests) > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum 100 hands per batch request",
        )

    results = []
    for idx, request in enumerate(requests):
        try:
            cards = [Card(rank=r, suit=s) for r, s in request.cards]
            hand = Hand(cards=cards)
            hand_type = HandClassifier.classify(hand)
            formatted_cards = [str(card) for card in hand.cards]

            results.append(
                ClassifyResponse(
                    hand_type=str(hand_type),
                    strength=hand_type.value,
                    cards=formatted_cards,
                )
            )
        except (ValidationError, ValueError) as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Invalid hand at index {idx}: {str(e)}",
            ) from e

    return results


@router.post(
    "/compare",
    response_model=CompareResponse,
    status_code=status.HTTP_200_OK,
    summary="Compare Two Poker Hands",
    description="Compare two poker hands and determine which is stronger",
)
async def compare_hands(request: CompareRequest) -> CompareResponse:
    """
    Compare two poker hands.

    Args:
        request: CompareRequest with two hands

    Returns:
        CompareResponse indicating winner and both classifications

    Raises:
        HTTPException: If validation fails
    """
    try:
        # Create hands
        cards1 = [Card(rank=r, suit=s) for r, s in request.hand1]
        cards2 = [Card(rank=r, suit=s) for r, s in request.hand2]

        hand1 = Hand(cards=cards1)
        hand2 = Hand(cards=cards2)

        # Classify both
        type1 = HandClassifier.classify(hand1)
        type2 = HandClassifier.classify(hand2)

        # Create responses
        response1 = ClassifyResponse(
            hand_type=str(type1),
            strength=type1.value,
            cards=[str(c) for c in hand1.cards],
        )

        response2 = ClassifyResponse(
            hand_type=str(type2),
            strength=type2.value,
            cards=[str(c) for c in hand2.cards],
        )

        # Determine winner
        if type1.value > type2.value:
            winner = "hand1"
        elif type2.value > type1.value:
            winner = "hand2"
        else:
            winner = "tie"

        return CompareResponse(winner=winner, hand1=response1, hand2=response2)

    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid hand: {str(e)}",
        ) from e
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e
