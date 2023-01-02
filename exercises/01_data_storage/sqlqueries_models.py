# Third party imports
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    """ Model class to represent a user """

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    created_time = Column(DateTime(timezone=True),
                          server_default=func.now())
    modified_time = Column(DateTime(timezone=True),
                           server_default=func.now(),
                           onupdate=func.now())

    # Relationship with other tables
    accounts = relationship('Account', secondary='user_account')

# end class User


class Account(Base):
    """ Account within the application to hold balance """

    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False)
    created_time = Column(DateTime(timezone=True),
                          server_default=func.now())
    modified_time = Column(DateTime(timezone=True),
                           server_default=func.now(),
                           onupdate=func.now())

    # Relationship with other tables
    users = relationship('User', secondary='user_account')

# end class Account


class UserAccount(Base):
    """ The association table to link User and Account """

    __tablename__ = 'user_account'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)

    # Relationship
    user = relationship('User', backref='account_association')
    account = relationship('Account', backref='user_association')

# end class UserAccount


class Transaction(Base):
    """ Association to the transactions """

    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey('account.id'))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String, nullable=False)
    created_time = Column(DateTime(timezone=True),
                          server_default=func.now())
    modified_time = Column(DateTime(timezone=True),
                           server_default=func.now(),
                           onupdate=func.now())

    # Relationship
    account = relationship('Account', backref='transactions')
    user = relationship('User', backref='transactions')

# end class Transaction
