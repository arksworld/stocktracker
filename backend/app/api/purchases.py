from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.purchase import StockPurchase
from app.schemas.purchase import CreatePurchaseRequest


router = APIRouter(prefix="/api/purchases", tags=["Purchases"])


@router.post("/{tracked_stock_id}")
def add_purchase(
    tracked_stock_id: int,
    payload: CreatePurchaseRequest,
    db: Session = Depends(get_db),
):
    purchase = StockPurchase(
        tracked_stock_id=tracked_stock_id,
        purchase_price=payload.purchase_price,
        quantity=payload.quantity,
        purchase_date=payload.purchase_date,
    )

    db.add(purchase)
    db.commit()
    db.refresh(purchase)

    return purchase