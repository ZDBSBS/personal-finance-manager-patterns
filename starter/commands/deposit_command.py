"""Command that deposits funds into an injected balance."""
from balance.balance import Balance
from commands.command import Command


class DepositCommand(Command):
    """Deposit an amount and provide an inverse operation."""

    def __init__(
        self, balance: Balance, amount: float, description: str = ""
    ) -> None:
        self.balance = balance
        self.amount = amount
        self.description = description

    def execute(self) -> None:
        self.balance.deposit(self.amount, self.description)

    def undo(self) -> None:
        self.balance.withdraw(self.amount, f"Undo: {self.description}".strip())
