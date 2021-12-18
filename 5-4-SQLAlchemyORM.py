from sqlalchemy import create_engine

engine = create_engine('mysql://root:@127.0.0.1:3306/my_data_base?charset=utf8')
