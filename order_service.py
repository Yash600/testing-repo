from payment_processor import charge_customer

def create_order(user_id: str, items: list) -> dict:
    total = sum(item["price"] for item in items)
    payment = charge_customer(user_id, total, "USD")
    return {
        "user_id": user_id,
        "total": total,
        "status": "paid",
        "transaction_id": payment["transaction_id"],
    }

def reorder(user_id: str, previous_items: list) -> dict:
    return create_order(user_id, previous_items)
