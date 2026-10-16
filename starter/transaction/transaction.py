"""Internal transaction model."""

from typing import Optional

from transaction.transaction_category import TransactionCategory


class Transaction:
    """Represents income or expense in the internal transaction format."""

    def __init__(
        self,
        amount: float,
        category: Optional[TransactionCategory] = None,
        description: str = "",
        *,
        transaction_type: Optional[str] = None,
    ) -> None:
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        if category is None and transaction_type is not None:
            category = self._category_from_type(transaction_type)
        if category is None:
            raise ValueError(
                "A transaction category or transaction_type is required")
        self.amount = amount
        self.category = category
        self.description = description

    @staticmethod
    def _category_from_type(transaction_type: str) -> TransactionCategory:
        categories = {
            "income": TransactionCategory.INCOME,
            "expense": TransactionCategory.EXPENSE,
        }
        try:
            return categories[transaction_type.lower()]
        except (AttributeError, KeyError):
            raise ValueError(
                "transaction_type must be 'income' or 'expense'") from None

    @property
    def transaction_type(self) -> str:
        """Return the normalized type name used by external interfaces."""
        if self.category == TransactionCategory.INCOME:
            return "income"
        if self.category == TransactionCategory.EXPENSE:
            return "expense"
        raise ValueError("Transaction category must be INCOME or EXPENSE")

    def __str__(self) -> str:
        return f"Transaction(${self.amount}, category='{self.category}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Transaction):
            return NotImplemented
        return self.amount == other.amount and self.category == other.category
