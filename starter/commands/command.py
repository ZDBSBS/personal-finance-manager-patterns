"""Command interface for reversible balance operations."""
from abc import ABC, abstractmethod


class Command(ABC):
    """Interface for an operation that can be executed and undone."""

    @abstractmethod
    def execute(self) -> None:
        """Apply the operation."""

    @abstractmethod
    def undo(self) -> None:
        """Reverse the operation."""
