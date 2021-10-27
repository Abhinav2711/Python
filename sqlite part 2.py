import pandas as pd

con=sqlite3.connect('test')
df=pd.read_sql_query("select*from test",con)
print(type(df))
print(df.shape)
print(df.head())
con.close()
