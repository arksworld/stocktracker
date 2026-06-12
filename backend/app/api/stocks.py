from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.stock import Stock
from app.schemas.stock import CreateStockRequest


router = APIRouter(prefix="/api/stocks", tags=["Stocks"])


@router.get("")
def get_stocks(db: Session = Depends(get_db)):
    return db.query(Stock).all()


@router.post("")
def create_stock(
    payload: CreateStockRequest,
    db: Session = Depends(get_db),
):
    stock = Stock(
        stock_code=payload.stock_code,
        stock_name=payload.stock_name,
        exchange=payload.exchange,
    )

    db.add(stock)
    db.commit()
    db.refresh(stock)

    return stock