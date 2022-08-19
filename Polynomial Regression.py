#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.linear_model import LinearRegression


# In[2]:


from sklearn.preprocessing import PolynomialFeatures


# In[3]:


x=np.array([5,15,25,35,45,55]).reshape((-1,1))
y=np.array([15,11,2,8,25,32])


# In[4]:


transformer=PolynomialFeatures(degree=2,include_bias=False)
transformer.fit(x,y)


# In[5]:


x_=transformer.transform(x)


# In[6]:


#x_=PolynomialFeatures()(degree=2,include_bias=False)transformer.fit(x,y)
model=LinearRegression().fit(x_,y)


# In[7]:


r_sq=model.score(x_,y)
print(f"coefficient of determination:{r_sq}")
print(f"intercept:{model.intercept_}")
print(f"scope:{model.coef_}")


# In[8]:


y_pred=model.predict(x_)
print(f"predicted response:/n{y_pred}")


# In[ ]:




