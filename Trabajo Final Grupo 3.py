#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df1 = pd.read_excel('CUSTOMERS NORTHWIND.xlsx')
#df1.shape
df1


# In[2]:


import pandas as pd
df2 = pd.read_json('CUSTOMERS NORTHWIND.json')
#df2.shape
df2


# In[3]:


import pandas as pd
df3 = pd.read_csv('CUSTOMERS-NORTHWIND.csv',delimiter=',',encoding='unicode_escape')
print(df3)


# In[4]:


import pandas as pd
df4 = pd.read_csv('CUSTOMERS-NORTHWIND.txt',delimiter=';',encoding='unicode_escape')
print(df4)


# In[5]:


import pandas as pd
df5 = pd.read_csv('CUSTOMERS-NORTHWIND.dat',delimiter=',',encoding='unicode_escape')
print(df5)


# In[1]:


import pandas as pd
df=pd.read_csv('CUSTOMERS-NORTHWIND.csv',delimiter=',')
#df
df5=df[df.ContactTitle=="Owner"]
df5


# In[2]:


import sqlalchemy as sa
import pyodbc
import urllib
import pandas as pd

params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=JOSE\SQLEXPRESS;DATABASE=northwind;UID=sa;PWD=123456')
engine = sa.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
#standard connection string
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

#the command to send your dataframe to SQL Server. 
df5.to_sql(name='CopiaCustomers',schema= 'dbo', con=engine, if_exists='replace',index=False, chunksize = 1000)


# In[ ]:




