from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/spider')

sql = 'select email from users where email="123@163.com"'
df=pd.read_sql_query(sql,engine)
for i in list(df['email']):
    print(i)


