from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/flask_news'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable=False, comment='标题')
    img_url = db.Column(db.String(200), nullable=False, comment='主图地址')
    content = db.Column(db.String(200), nullable=False, comment='新闻内容')
    is_valid = db.Column(db.Boolean, default=True, comment='逻辑删除')
    created_at = db.Column(db.DateTime, default=datetime.now(), comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.now(), comment='最后修改时间')
    news_type = db.Column(db.Enum('本地', '百家', '娱乐', '军事'), comment='新闻类别')


# class User(db.Model):
#     __tablename__ = 'account_user'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(32), nullable=False)


# 映射
db.drop_all()
db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
