import unittest
from transaction.external_income_transaction import ExternalFreelanceIncome
from transaction.transaction_adapter import TransactionAdapter
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TestTransactionAdapter(unittest.TestCase):

    def test_adapter_converts_freelance_income(self):
        ext_txn = ExternalFreelanceIncome(
            500, "INV-12345", "Website development")
        adapter = TransactionAdapter(ext_txn)
        txn = adapter.to_transaction()
        self.assertEqual(txn, Transaction(500, TransactionCategory.INCOME))
        self.assertEqual(txn.description, "Website development")

    def test_adapter_accepts_external_payment_amount_format(self):
        external_income = ExternalFreelanceIncome(
            income_source="Upwork", payment_amount=500
        )
        transaction = TransactionAdapter(external_income).to_transaction()

        self.assertEqual(external_income.payment_amount, 500)
        self.assertEqual(external_income.transaction_type, "income")
        self.assertEqual(transaction.amount, 500)
        self.assertEqual(transaction.transaction_type, "income")
        self.assertEqual(transaction.description, "")


if __name__ == "__main__":
    unittest.main()
