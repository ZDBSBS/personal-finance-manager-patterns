"""This module serves as the entry point for the program."""
from balance.balance import Balance
from balance.balance_observer import (
    LowBalanceAlertObserver,
    PrintBalanceObserver,
)
from commands.command_manager import CommandManager
from commands.deposit_command import DepositCommand
from commands.withdraw_command import WithdrawCommand
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_adapter import TransactionAdapter
from transaction.external_income_transaction import ExternalFreelanceIncome


def main() -> None:
    """Run a short demonstration of the finance manager patterns."""
    balance = Balance.get_instance()
    balance.reset()
    balance.attach(LowBalanceAlertObserver(threshold=100))
    balance.attach(PrintBalanceObserver())
    manager = CommandManager()

    print("Adding transactions...")
    transactions = [
        Transaction(100, TransactionCategory.INCOME, "Initial payment"),
        Transaction(50, TransactionCategory.EXPENSE, "Supplies"),
        Transaction(200, TransactionCategory.INCOME, "Project milestone"),
        Transaction(75, TransactionCategory.EXPENSE, "Travel"),
    ]

    freelance_income = ExternalFreelanceIncome(
        payment_amount=1200,
        invoice_id="INV-98765",
        description="Mobile App Project",
        income_source="Freelance platform",
    )
    adapter = TransactionAdapter(freelance_income)
    adapted_transaction = adapter.to_transaction()

    for transaction in transactions + [adapted_transaction]:
        command_type = (
            DepositCommand
            if transaction.category == TransactionCategory.INCOME
            else WithdrawCommand
        )
        manager.execute(
            command_type(balance, transaction.amount, transaction.description)
        )

    print("Undoing last transaction...")
    manager.undo()
    print("Redoing last transaction...")
    manager.redo()
    print(balance.summary())


if __name__ == "__main__":
    main()
