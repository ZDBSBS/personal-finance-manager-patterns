"""Adapter from third-party freelance income to internal transactions."""

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.external_income_transaction import ExternalFreelanceIncome


class TransactionAdapter:
    def __init__(self, external_transaction: ExternalFreelanceIncome) -> None:
        self.external_transaction = external_transaction

    def to_transaction(self) -> Transaction:
        """Convert an external transaction to a standard Transaction."""
        return Transaction(
            self.external_transaction.amount,
            TransactionCategory.INCOME,
            self.external_transaction.description,
        )
