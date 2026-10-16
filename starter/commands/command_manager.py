"""History manager for command execution, undo, and redo."""
from typing import List

from commands.command import Command


class CommandManager:
    """Manage command history using injected command objects."""

    def __init__(self) -> None:
        self._history: List[Command] = []
        self._redo_history: List[Command] = []

    def execute(self, command: Command) -> None:
        """Execute a command and record it for undo."""
        command.execute()
        self._history.append(command)
        self._redo_history.clear()

    def undo(self) -> bool:
        """Undo the latest command; return False when history is empty."""
        if not self._history:
            return False
        command = self._history[-1]
        command.undo()
        self._history.pop()
        self._redo_history.append(command)
        return True

    def redo(self) -> bool:
        """
        Redo the latest undone command.

        Return False when no command is available.
        """
        if not self._redo_history:
            return False
        command = self._redo_history[-1]
        command.execute()
        self._redo_history.pop()
        self._history.append(command)
        return True
