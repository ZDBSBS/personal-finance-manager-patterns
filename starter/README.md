# Personal Finance Manager

A small Python application for tracking freelancer income and expenses. It
demonstrates object-oriented design patterns while keeping observers and
commands injectable for straightforward testing.

## Patterns Used

- **Singleton:** `Balance` provides one application-wide balance instance.
- **Adapter:** `TransactionAdapter` converts freelance-platform payments into
  internal `Transaction` objects.
- **Observer:** `LowBalanceAlertObserver` and `PrintBalanceObserver` respond to
  balance changes.
- **Command:** `DepositCommand`, `WithdrawCommand`, and `CommandManager` support
  execute, undo, and redo operations.

## Requirements

Python 3.10 or later. Install the test dependency with:

```text
python -m pip install -r requirements.txt
```

## How To Run

From this directory:

```text
python main.py
```

## How To Run Tests

```text
pytest
```

The tests can also be run with Python's standard test runner:

```text
python -m unittest discover
```

See [docs/reflection.md](docs/reflection.md) for a short discussion of the
pattern choices and implementation challenges.
