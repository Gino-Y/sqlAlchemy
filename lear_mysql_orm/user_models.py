"""
用户地址信息的OEM模型
"""
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """用户信息表"""
    __tablename__ = 'account_user'
    id = Column('id')


class UserAddress(Base):
    """用户地址信息表"""
    __tablename__ = 'account_user_address'

