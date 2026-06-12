from typing import Iterable


def calculate_average_price(purchases: Iterable) -> float:
    total_cost = sum(float(p.purchase_price) * float(p.quantity) for p in purchases)
    total_quantity = sum(float(p.quantity) for p in purchases)

    if total_quantity == 0:
        return 0

    return round(total_cost / total_quantity, 2)