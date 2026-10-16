"""Balance observers for printing updates and warning about low funds."""
from transaction.transaction import Transaction


class IBalanceObserver:
    """Interface implemented by balance observers."""

    def update(self, balance: float, transaction: Transaction) -> None:
        """Handle balance updates."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    """Print the balance after each transaction."""

    def update(self, balance: float, transaction: Transaction) -> None:
        """Print balance update message."""
        print(f"Current Balance: {balance:g} €")


class PrintBalanceObserver(PrintObserver):
    """Explicitly named print observer."""


class LowBalanceAlertObserver(IBalanceObserver):
    """Track whether the balance is below a configured threshold."""

    def __init__(self, threshold: float) -> None:
        self.threshold = threshold
        self.alert_triggered = False

    def update(self, balance: float, transaction: Transaction) -> None:
        """Alert if balance drops below threshold."""
        self.alert_triggered = balance < self.threshold
        if self.alert_triggered:
            print(f"WARNING: Balance below {self.threshold:g} €")
