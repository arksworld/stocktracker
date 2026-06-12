from pydantic import BaseModel


class CreateStockRequest(BaseModel):
    stock_code: str
    stock_name: str | None = None
    exchange: str | None = None