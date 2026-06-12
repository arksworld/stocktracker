from datetime import datetime
from datetime import timezone

import httpx
from sqlalchemy.orm import Session

from app.models.stock import Stock
from app.models.stock_price import StockPrice


class MarketDataService:
    API_URL = "https://www.alphavantage.co/query"

    #API_KEY="MBQZHVNACJFZE2DA"
    @staticmethod
    async def sync_stock_price(db: Session, stock: Stock):
        price = 100.0

        stock_price = StockPrice(
            stock_id=stock.id,
            market_price=price,
            source="mock",
            price_timestamp=datetime.now(timezone.utc),
        )

        db.add(stock_price)
        db.commit()