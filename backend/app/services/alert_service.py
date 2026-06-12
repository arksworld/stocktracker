from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.alert_rule import AlertRule
from app.models.stock_price import StockPrice


class AlertService:
    @staticmethod
    def evaluate_alerts(db: Session):
        rules = db.query(AlertRule).filter(AlertRule.is_active.is_(True)).all()

        for rule in rules:
            latest_price = (
                db.query(StockPrice)
                .filter(StockPrice.stock_id == rule.tracked_stock_id)
                .order_by(StockPrice.price_timestamp.desc())
                .first()
            )

            if not latest_price:
                continue

            triggered = False

            if rule.operator == "ABOVE":
                triggered = (
                    float(latest_price.market_price)
                    > float(rule.threshold_value)
                )

            if rule.operator == "BELOW":
                triggered = (
                    float(latest_price.market_price)
                    < float(rule.threshold_value)
                )

            if triggered:
                alert = Alert(
                    alert_rule_id=rule.id,
                    triggered_price=latest_price.market_price,
                    message=f"Alert triggered for rule {rule.id}",
                )

                db.add(alert)

        db.commit()