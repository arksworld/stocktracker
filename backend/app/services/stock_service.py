from sqlalchemy.orm import Session

from app.models.purchase import StockPurchase
from app.models.stock import Stock
from app.models.stock_price import StockPrice
from app.models.tracked_stock import TrackedStock
from app.utils.calculations import calculate_average_price


class StockService:
    @staticmethod
    def get_dashboard(db: Session, user_id: int):
        tracked = (
            db.query(TrackedStock)
            .filter(TrackedStock.user_id == user_id)
            .all()
        )

        response = []

        for item in tracked:
            stock = db.query(Stock).filter(Stock.id == item.stock_id).first()

            purchases = (
                db.query(StockPurchase)
                .filter(StockPurchase.tracked_stock_id == item.id)
                .all()
            )

            latest_price = (
                db.query(StockPrice)
                .filter(StockPrice.stock_id == stock.id)
                .order_by(StockPrice.price_timestamp.desc())
                .first()
            )

            avg_price = calculate_average_price(purchases)
            current_price = float(latest_price.market_price) if latest_price else 0

            percentage = 0

            if avg_price > 0:
                percentage = round(
                    ((current_price - avg_price) / avg_price) * 100,
                    2,
                )

            response.append(
                {
                    "stock": stock.stock_code,
                    "avg_price": avg_price,
                    "current_price": current_price,
                    "performance": percentage,
                }
            )

        return response