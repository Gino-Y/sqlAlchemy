"""
用户地址信息的OEM模型
"""
from datetime import datetime
from enum import IntEnum
from sqlalchemy import Column, Integer, String, Enum, SmallInteger,Boolean, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SexEnum(IntEnum):
    MAN = 1
    WOMEN = 0


class User(Base):
    """用户信息表"""
    __tablename__ = 'account_user'
    id = Column('id', type_=Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True, comment='用户名')
    password = Column(String(32), nullable=False, comment='密码')
    real_name = Column(String(16), comment='真实姓名')
    sex = Column(Enum(SexEnum), default=None, comment='性别')
    age = Column(SmallInteger, default=0, comment='年龄')
    created_at = Column(DateTime, default=datetime.now(), comment='创建时间')
    is_valid = Column(Boolean, default=True, comment='是否有效')


class UserAddress(Base):
    """用户地址信息表"""
    __tablename__ = 'account_user_address'

    id = Column('id', type_=Integer, primary_key=True)
    area = Column(String(256), nullable=False, comment='地址信息')
    phone_no = Column(String(11), comment='电话号码')
    remark = Column(String(512), comment='备注信息')
    created_at = Column(DateTime, default=datetime.now(), comment='创建时间')
    is_valid = Column(Boolean, default=True, comment='是否有效')


