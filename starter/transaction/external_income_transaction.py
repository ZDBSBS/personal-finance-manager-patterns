"""External freelance income model."""
from typing import Optional


class ExternalFreelanceIncome:
    """Represents income received from a third-party freelance platform."""

    def __init__(
        self,
        amount: Optional[float] = None,
        invoice_id: str = "",
        description: str = "",
        income_source: str = "",
        *,
        payment_amount: Optional[float] = None,
    ) -> None:
        if amount is not None and payment_amount is not None:
            raise ValueError("Specify either amount or payment_amount, not both")
        self.amount = payment_amount if payment_amount is not None else amount
        if self.amount is None:
            raise ValueError("An amount or payment_amount is required")
        self.payment_amount = self.amount
        self.invoice_id = invoice_id
        self.description = description
        self.income_source = income_source
        self.typ = "income"
        self.transaction_type = "income"
