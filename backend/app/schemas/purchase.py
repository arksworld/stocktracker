from datetime import date

from pydantic import BaseModel


class CreatePurchaseRequest(BaseModel):
    purchase_price: float
    quantity: float
    purchase_date: date