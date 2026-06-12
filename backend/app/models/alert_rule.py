from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.sql import func

from app.core.database import Base


class AlertRule(Base):
    __tablename__ = "alert_rules"

    id = Column(Integer, primary_key=True, index=True)

    tracked_stock_id = Column(
        Integer,
        ForeignKey("tracked_stocks.id"),
        nullable=False,
    )

    rule_type = Column(String(50), nullable=False)
    operator = Column(String(20), nullable=False)
    threshold_value = Column(Numeric(12, 2), nullable=False)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
