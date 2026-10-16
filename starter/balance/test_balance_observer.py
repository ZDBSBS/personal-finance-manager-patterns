import unittest
from contextlib import redirect_stdout
from io import StringIO

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from balance.balance import Balance
from balance.balance_observer import (
    LowBalanceAlertObserver,
    PrintBalanceObserver,
)


class TestLowBalanceAlertObserver(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()
        for observer in tuple(self.balance._observers):
            self.balance.detach(observer)

    def test_alert_triggers_on_low_balance(self):
        observer = LowBalanceAlertObserver(threshold=50)
        self.balance.register_observer(observer)

        self.balance.apply_transaction(
            Transaction(100, TransactionCategory.INCOME))
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE))
        self.assertTrue(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(100, TransactionCategory.INCOME))
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE))
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE))
        self.assertTrue(observer.alert_triggered)

    def test_print_observer_reports_updated_balance(self):
        observer = PrintBalanceObserver()
        self.balance.attach(observer)
        output = StringIO()

        with redirect_stdout(output):
            self.balance.apply_transaction(
                Transaction(1250, TransactionCategory.INCOME)
            )

        self.assertIn("Current Balance: 1250 €", output.getvalue())

    def test_observer_can_be_detached(self):
        observer = LowBalanceAlertObserver(threshold=50)
        self.balance.attach(observer)
        self.balance.detach(observer)

        self.balance.apply_transaction(
            Transaction(10, TransactionCategory.INCOME)
        )

        self.assertFalse(observer.alert_triggered)


if __name__ == "__main__":
    unittest.main()
