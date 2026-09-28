import pytest
from bank import BankAccount


@pytest.fixture
def account():
    print("[setup]")
    bank_account = BankAccount(100)

    yield bank_account

    print("[teardown]")


def test_initial_balance(account):
    assert account.balance == 100


def test_deposit_with_teardown(account):
    account.deposit(50)
    assert account.balance == 150