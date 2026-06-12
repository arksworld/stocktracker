from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.dashboard import router as dashboard_router
from app.api.purchases import router as purchases_router
from app.api.stocks import router as stocks_router
from app.core.database import Base
from app.core.database import engine
from app.core.scheduler import scheduler


Base.metadata.create_all(bind=engine)

app = FastAPI(title="StockTracker API")

app.include_router(auth_router)
app.include_router(stocks_router)
app.include_router(purchases_router)
app.include_router(dashboard_router)


@app.on_event("startup")
def startup_event():
    scheduler.start()


@app.get("/")
def health_check():
    return {"status": "ok"}