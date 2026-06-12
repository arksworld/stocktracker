from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String

from app.core.database import Base


class StockPrice(Base):
    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    market_price = Column(Numeric(12, 2), nullable=False)
    source = Column(String(50))
    price_timestamp = Column(DateTime(timezone=True), nullable=False)