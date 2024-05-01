#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

big data exercises 
Erick Heredia

"""


# In[116]:


import sqlite3
import pandas as pd 


# In[119]:


database = sqlite3.connect("books.db")


# In[144]:


book_db = database.cursor()

book_db.execute("SELECT title FROM titles")

des = book_db.description

data = book_db.fetchall()

print(des, "\n")

print(data)


# In[131]:


pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors ORDER BY Last DESC ', database, index_col=['id'])


# In[77]:


pd.read_sql('SELECT * FROM titles ORDER BY title ASC', database)


# In[40]:


cursor = database.cursor()

cursor = cursor.execute("""INSERT INTO authors(first, last) 
VALUES ('James','bond')""")

pd.read_sql('SELECT * FROM authors', database, index_col=['id'])


# In[55]:


cursor = cursor.execute(""" INSERT INTO titles(title, isbn, edition, copyright)
VALUES('how to be a spy','234567890','1','2024')""")

pd.read_sql('SELECT * FROM titles', database)


# In[114]:


database.close()


# In[ ]:




