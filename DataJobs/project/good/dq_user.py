import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/spider')

def dq_user():
    sql3 = 'select email from dq_user'
    m_data3 = pd.read_sql_query(sql3, engine)
    if len((list(m_data3['email']))) > 0:
        sql4 = 'select name from users where email="{}"'.format((list(m_data3['email']))[0])
        df = pd.read_sql_query(sql4, engine)
        m_data4 = (list(df['name']))[0]
        return m_data4
    else:
        return ''
