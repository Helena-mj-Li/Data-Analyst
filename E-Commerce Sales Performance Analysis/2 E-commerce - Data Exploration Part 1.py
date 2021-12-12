#!/usr/bin/env python
# coding: utf-8

# ### Join all the data

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import pandas_profiling


# In[2]:


aisles = pd.read_csv("aisles.csv")
departments = pd.read_csv("departments.csv")
order_products = pd.read_csv("order_products.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")


# In[3]:


aisles.info()


# In[4]:


departments.info()


# In[5]:


order_products.info()


# In[6]:


orders.info()


# In[7]:


products.info()


# In[8]:


print(aisles.shape)
print(departments.shape)
print(order_products.shape)
print(orders.shape)
print(products.shape)


# In[9]:


aisles_products = pd.merge(aisles, products, on = "aisle_id")
aisles_products.info()


# In[10]:


aisles_products.shape


# In[11]:


ord_prod_ord = pd.merge(order_products, orders, on = "order_id")
ord_prod_ord.info()


# In[12]:


ord_prod_ord.shape


# In[13]:


ais_prod_depart = pd.merge(aisles_products, departments, on="department_id")
ais_prod_depart.info()


# In[14]:


ais_prod_depart.shape


# In[15]:


new = pd.merge(ais_prod_depart, ord_prod_ord, on = "product_id")
new.info()


# In[16]:


new.shape


# In[17]:


new.info()


# In[18]:


new.describe()    


# In[19]:


new.describe(include = ['O'])             #crime.describe(include=['O'])


# In[20]:


new.head()


# In[21]:


new.boxplot()


# In[22]:


new.boxplot(column = 'add_to_cart_order')


# In[23]:


new.boxplot(column = ['add_to_cart_order', 'aisle_id'])


# ### Plot the distribution of numeric columns

# In[24]:


#pandas_profiling.ProfileReport(new)   - data profiling


# In[26]:


new.duplicated(subset=None, keep=False)


# In[27]:


new = new.drop_duplicates(keep='first')


# In[28]:


new['aisle'].value_counts()


# In[29]:


plt.figure(figsize=(16,8))
new['aisle'].value_counts().head(8).plot.bar()
plt.show()


# In[30]:


plt.figure(figsize=(15,14))
aisle = new['aisle'].value_counts().reset_index()
plt.bar(aisle['index'][0:5], aisle['aisle'][0:5])


# In[31]:


new['product_name'].value_counts()


# In[32]:


# bar chart
plt.figure(figsize=(16,8))
new['product_name'].value_counts().head(5).plot.bar()
plt.show()


# In[33]:


#another way to show the bar chart
plt.figure(figsize=(15,14))
product_name = new['product_name'].value_counts().reset_index()
plt.bar(product_name['index'][0:5], product_name['product_name'][0:5])


# In[30]:


new['department'].value_counts()


# In[31]:


#distribution
plt.figure(figsize=(16,8))
new['department'].value_counts().head(8).plot.bar()
plt.show()


# In[32]:


# bar chart
department = new['department'].value_counts().reset_index()
plt.figure(figsize=(15,14))
plt.bar(department['index'][0:5], department['department'][0:5])


# In[33]:


new['order_number'].value_counts()


# In[34]:


plt.figure(figsize=(16,8))
new['order_number'].value_counts().head(5).plot.bar()
plt.show()


# In[35]:


# another way to show bar chart
plt.figure(figsize=(15,14))
order_number = new['order_number'].value_counts().reset_index()
plt.bar(order_number['index'][0:5], order_number['order_number'][0:5])


# In[36]:


new['order_dow'].value_counts()


# In[37]:


plt.figure(figsize=(16,8))
new['order_dow'].value_counts().plot.bar()
plt.show()


# In[38]:


# another way to show bar chart
plt.figure(figsize=(15,14))
order_dow = new['order_dow'].value_counts().reset_index()
plt.bar(order_dow['index'][0:7], order_dow['order_dow'][0:7])


# In[39]:


plt.figure(figsize=(16,8))
new['order_hour_of_day'].value_counts().head(7).plot.bar()
plt.show()


# In[40]:


# another way to show bar chart
plt.figure(figsize=(15,14))
order_hour_of_day = new['order_hour_of_day'].value_counts().reset_index()
plt.bar(order_hour_of_day['index'][0:6], order_hour_of_day['order_hour_of_day'][0:6])


# In[20]:


sns.countplot("order_dow", hue = "department", data = new)   # 把横轴调节大一些


# In[22]:


labels = new['department'].unique().tolist()
counts = new['department'].value_counts()
sizes = [counts[var_cat] for var_cat in labels]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels,  autopct='%1.1f%%',shadow=True) 
ax1.axis('equal')
plt.show()


# In[26]:


plt.figure(figsize=(16,9))
new.groupby('department')['order_dow'].count().plot(marker = 'o')
plt.ylabel('department')
plt.title('Retail Distribution')
plt.show()               #对不对是一个问题，需不需要这样做是一个问题。有没有商业价值。
                         # 线图一般应用于时间序列，订单序列 sequential number。来展示随着时间的发展，数据的规律。 
                         #横轴选择季节，时间date, processed 的时间序列。线性图。


# In[44]:


sns.catplot(x="department",
            hue="order_dow",
            col="aisle",
            data=new,
            kind="count"
            )        #对于aisle 画一个bar plot， top 10 就可以了
                     # 商业数据中不需要把所有的数据都显示出来，前十个，最重要的几个。top 10, bottom 10卖的最好的，最差的。
                     # 商业中业务需要看什么？数据分析师需要把对方的需求转化为技术和数据。一定要充分理解业务。技术上把图画
                     # 出来，但是应用于业务、商业中，要make sense


# ### Create box-plot on numeric columns

# In[47]:


product_id = new['product_id']
sns.boxplot(product_id)           #没有太多商业意义


# In[53]:


add_to_cart_order = new['add_to_cart_order']
sns.boxplot(add_to_cart_order)         #离散状态，异常值，outlayer


# In[48]:


department_id = new['department_id']
sns.boxplot(department_id)         #没有太多商业价值


# In[49]:


order_dow = new['order_dow']
sns.boxplot(order_dow)                #没有商业价值


# In[50]:


order_hour_of_day = new['order_hour_of_day']
sns.boxplot(order_hour_of_day)               #没有商业价值。能代表什么意义呢？


# In[51]:


days_since_prior_order = new['days_since_prior_order']
sns.boxplot(days_since_prior_order)


# In[ ]:





# In[ ]:




