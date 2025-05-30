from uuid import UUID, uuid4
from dataclasses import dataclass, field

@dataclass(frozen=True)
class CreateExpenseCommand:
    action: str
    description: str
    amount: float
    payment_method: str