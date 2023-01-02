# Third party imports
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Application imports
from sqlqueries import get_user, get_accounts_by_user, compute_balance, debit
from sqlqueries_models import Base, User, Account, UserAccount, Transaction


@pytest.fixture(scope='function')
def setup_database():

    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

# end setup_database()


@pytest.fixture(scope='function')
def dataset(setup_database):

    session = setup_database

    # Creates user
    john = User(username='john')
    mary = User(username='mary')
    session.add(john)
    session.add(mary)
    session.commit()

    # Creates account
    john_account = Account(balance=10.0)
    mary_account = Account(balance=5.0)
    joint_account = Account(balance=20.0)
    john.accounts.append(john_account)
    mary.accounts.append(mary_account)
    john.accounts.append(joint_account)
    mary.accounts.append(joint_account)
    session.add(john_account)
    session.add(mary_account)
    session.add(joint_account)
    session.commit()

    yield session

# end dataset_1


def test_database(dataset):

    # Gets the session from the fixture
    session = dataset

    # Do some basic checking
    assert len(session.query(User).all()) == 2
    assert len(session.query(Account).all()) == 3
    assert len(session.query(UserAccount).all()) == 4

    # Retrieves John and Mary
    john = get_user('john', session)
    mary = get_user('mary', session)

    # Checks their accounts
    assert len(get_accounts_by_user(john.username, session)) == 2
    assert len(get_accounts_by_user(mary.username, session)) == 2

    # Checks the balance
    assert compute_balance(john.username, session) == 30.0
    assert compute_balance(mary.username, session) == 25.0

    # Attemps to debit from the joint account, i.e index 1
    joint_account = get_accounts_by_user(john.username, session)[1]
    debit(joint_account.id, 10.0, session)
    assert compute_balance(john.username, session) == 20.0
    assert compute_balance(mary.username, session) == 15.0

# end test_database()
