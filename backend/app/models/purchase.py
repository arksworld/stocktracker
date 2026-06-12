from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy.sql import func

from app.core.database import Base


class StockPurchase(Base):
    __tablename__ = "stock_purchases"

    id = Column(Integer, primary_key=True, index=True)

    tracked_stock_id = Column(
        Integer,
        ForeignKey("tracked_stocks.id"),
        nullable=False,
    )

    purchase_price = Column(Numeric(12, 2), nullable=False)
    quantity = Column(Numeric(12, 2), nullable=False)
    purchase_date = Column(Date, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())