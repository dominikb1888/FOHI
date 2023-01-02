# Standard imports
from typing import List

# Third party imports
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

# Application imports
from sqlqueries_models import Account, User, Transaction


def get_user(username: str, session: Session) -> User:
    """ Gets the user by username """

    try:
        user = session.query(User).filter(User.username == username).one()
        return user
    except NoResultFound:
        return None

# end get_user()


def get_accounts_by_user(username: str, session: Session) -> List[Account]:
    """ Retrieves the accounts given the username """

    user = get_user(username, session)
    accounts = list(session.query(Account).filter(
        Account.users.contains(user)).all())
    return accounts

# end get_accounts_by_user


def compute_balance(username: str, session: Session) -> float:
    """ Computes the balance based on the username """

    accounts = get_accounts_by_user(username, session)
    balance = sum([account.balance for account in accounts])
    return balance

# end compute_balance()


def debit(account_id: int, amount: float, session: Session) -> float:
    """ Debits amount into the account """

    try:
        account = session.query(Account).filter(Account.id == account_id).one()
        account.balance -= amount
        transaction = Transaction(account_id=account_id,
                                  amount=amount,
                                  transaction_type='DEBIT')
        session.add(transaction)
        session.commit()
        return account.balance
    except NoResultFound:
        return 0

# end debit()


def credit(account_id: int, amount: float, session: Session) -> float:
    """ Debits amount into the account """

    try:
        account = session.query(Account).filter(Account.id == account_id).one()
        account.balance += amount
        transaction = Transaction(account_id=account_id,
                                  amount=amount,
                                  transaction_type='CREDIT')
        session.add(transaction)
        session.commit()
        return account.balance
    except NoResultFound:
        return 0

# end credit()
