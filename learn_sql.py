from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite://'+'/home/lmp/test.db'
app.config["SQLALCHEMY_DATABASE_URL"] = 'mysql+pymysql://localhost:123456@127.0.0.1:3306/Local instance MySQL80Gino'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'qweewqqwe'

db = SQLAlchemy(app)

# 学生表
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Enum('男', '女'), nullable=False)
    phone = db.Column(db.String(11), nullable=True)

#课程表
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    # teacher =

#教师表
class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Enum('男', '女'), nullable=False)
    phone = db.Column(db.String(11), nullable=True)

# #成绩表
# class Grade(db.Model):
#     __tablename__ = 'grade'
#     id = db.Column(db.Integer, primary_key=True)
#     course_name =
#     grade =
#     student =


if __name__ == '__main__':
    db.create_all()

