from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.stock_service import StockService


router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])


@router.get("/performance")
def dashboard(db: Session = Depends(get_db)):
    return StockService.get_dashboard(db, user_id=1)