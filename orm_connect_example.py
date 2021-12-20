from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('mysql://root:@127.0.0.1:3306/learn_mysql?charset=utf8',
                       echo=True)

Base = declarative_base()

class Student(Base):
    """学生信息表"""
    __tablename__='student'
    id = Column(type_=Integer, name='id', primary_key=True)  # type_=可以省略
    stu_no = Column(Integer, nullable=False, comment='学号')
    stu_name = Column(String(16), nullable=False, comment='姓名')
    created_at = Column(DateTime, comment='注册时间')

def create_table():
    """同步数据库表"""
    Base.metadata.create_all(bind=engine)
