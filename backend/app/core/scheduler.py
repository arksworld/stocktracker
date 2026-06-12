from apscheduler.schedulers.background import BackgroundScheduler

from app.core.database import SessionLocal
from app.models.stock import Stock
from app.services.alert_service import AlertService
from app.services.market_data_service import MarketDataService


scheduler = BackgroundScheduler()


async def sync_prices():
    db = SessionLocal()

    try:
        stocks = db.query(Stock).all()

        for stock in stocks:
            await MarketDataService.sync_stock_price(db, stock)

        AlertService.evaluate_alerts(db)

    finally:
        db.close()


scheduler.add_job(sync_prices, "interval", minutes=5)