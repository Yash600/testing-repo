import uuid


def charge_customer(customer_id: str, amount: int, currency: str, idempotency_key: str) -> dict:
    transaction_id = str(uuid.uuid4())
    print(f"Charging {customer_id}: {amount} {currency}")
    return {
        "transaction_id": transaction_id,
        "status": "success",
        "amount": amount,
    }

def refund(transaction_id: str, amount: int) -> dict:
    print(f"Refunding {amount} cents for {transaction_id}")
    return { "refund_id": str(uuid.uuid4()), "status": "refunded" }
