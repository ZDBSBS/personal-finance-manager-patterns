"""Singleton balance model and observer subject."""
from typing import List

from balance.balance_observer import IBalanceObserver
from transaction.transaction_category import TransactionCategory
from transaction.transaction import Transaction


class Balance:
    """Singleton that tracks a balance and notifies injected observers."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "_initialized"):
            self.current_balance = 0.0
            self._observers: List[IBalanceObserver] = []
            self._initialized = True

    @classmethod
    def get_instance(cls) -> "Balance":
        """Return the application's single balance instance."""
        return cls()

    def reset(self) -> None:
        """Reset the balance without notifying observers."""
        self.current_balance = 0.0

    def deposit(self, amount: float, description: str = "") -> None:
        """Add a positive amount and notify observers."""
        self._change_balance(amount, TransactionCategory.INCOME, description)

    def withdraw(self, amount: float, description: str = "") -> None:
        """Subtract a positive amount and notify observers."""
        self._change_balance(amount, TransactionCategory.EXPENSE, description)

    def add_income(self, amount: float) -> None:
        """Compatibility method for depositing income."""
        self.deposit(amount)

    def add_expense(self, amount: float) -> None:
        """Compatibility method for withdrawing an expense."""
        self.withdraw(amount)

    def _change_balance(
        self,
        amount: float,
        category: TransactionCategory,
        description: str = "",
    ) -> None:
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        transaction = Transaction(amount, category, description)
        self.apply_transaction(transaction)

    def apply_transaction(self, transaction: Transaction) -> None:
        """Apply a transaction and notify every registered observer."""
        if transaction.category == TransactionCategory.INCOME:
            self.current_balance += transaction.amount
        elif transaction.category == TransactionCategory.EXPENSE:
            self.current_balance -= transaction.amount
        else:
            raise ValueError("Transaction category must be INCOME or EXPENSE")
        self.notify(transaction)

    def get_balance(self) -> float:
        """Return the current balance."""
        return self.current_balance

    def summary(self) -> str:
        """Return a formatted balance summary."""
        return f"Current Balance: {self.current_balance:g} €"

    def attach(self, observer: IBalanceObserver) -> None:
        """Register an observer, avoiding duplicate registrations."""
        if observer not in self._observers:
            self._observers.append(observer)

    def register_observer(self, observer: IBalanceObserver) -> None:
        """Compatibility alias for attach."""
        self.attach(observer)

    def detach(self, observer: IBalanceObserver) -> None:
        """Unregister an observer if it is currently registered."""
        if observer in self._observers:
            self._observers.remove(observer)

    def unregister_observer(self, observer: IBalanceObserver) -> None:
        """Compatibility alias for detach."""
        self.detach(observer)

    def notify(self, transaction: Transaction) -> None:
        """Notify a snapshot of registered observers about a balance change."""
        for observer in tuple(self._observers):
            observer.update(self.current_balance, transaction)
