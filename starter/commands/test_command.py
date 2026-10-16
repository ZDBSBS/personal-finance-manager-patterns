"""Tests for command execution and command history."""
import unittest

from balance.balance import Balance
from commands.command_manager import CommandManager
from commands.deposit_command import DepositCommand
from commands.withdraw_command import WithdrawCommand


class TestCommandManager(unittest.TestCase):
    def setUp(self) -> None:
        self.balance = Balance.get_instance()
        self.balance.reset()
        self.manager = CommandManager()

    def test_execute_undo_and_redo_deposit(self) -> None:
        command = DepositCommand(self.balance, 250, "Client payment")
        self.manager.execute(command)
        self.assertEqual(self.balance.get_balance(), 250)

        self.assertTrue(self.manager.undo())
        self.assertEqual(self.balance.get_balance(), 0)

        self.assertTrue(self.manager.redo())
        self.assertEqual(self.balance.get_balance(), 250)

    def test_withdraw_command_and_new_command_clears_redo(self) -> None:
        self.manager.execute(DepositCommand(self.balance, 100))
        self.manager.execute(WithdrawCommand(self.balance, 30))
        self.assertEqual(self.balance.get_balance(), 70)

        self.assertTrue(self.manager.undo())
        self.assertEqual(self.balance.get_balance(), 100)
        self.manager.execute(DepositCommand(self.balance, 10))

        self.assertFalse(self.manager.redo())
        self.assertEqual(self.balance.get_balance(), 110)

    def test_empty_history_operations_return_false(self) -> None:
        self.assertFalse(self.manager.undo())
        self.assertFalse(self.manager.redo())


if __name__ == "__main__":
    unittest.main()
