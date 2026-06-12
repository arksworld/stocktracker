from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import Text
from sqlalchemy.sql import func

from app.core.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    alert_rule_id = Column(
        Integer,
        ForeignKey("alert_rules.id"),
        nullable=False,
    )

    triggered_price = Column(Numeric(12, 2))
    message = Column(Text)
    is_read = Column(Boolean, default=False)
    triggered_at = Column(DateTime(timezone=True), server_default=func.now())