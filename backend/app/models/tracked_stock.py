from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.sql import func

from app.core.database import Base


class TrackedStock(Base):
    __tablename__ = "tracked_stocks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
