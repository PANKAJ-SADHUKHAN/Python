#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[18]:


keepdims=False


# In[19]:


speed=[20,42,31,23,47,59,40,42,46]
a1=np.array(speed)
print(a1)


# In[20]:


#Mean=Average value in teh list
Mean=np.mean(a1)
print(Mean)


# In[21]:


#Meadian=The mid point value
Median=np.median(a1)
print(Median)


# In[22]:


#Mode=Most common element.
#scipy (Scientific Python) has a method mode().
# we have to install First scipy and import stats module.
from scipy import stats
Mode=stats.mode(a1)
print(Mode)
#in this case a1 42 is the most common element with occurence 2


# In[23]:


#lets take an list of the height of students(most common example)
height=[5.0,5.7,5.5,5.3,5.5,5.3,5.8,5.6]
#here 5.5 and 5.3 is the most common element
#so let's check what Mode function prints coresponding to thi height list
a2=np.array(height)
# or we can direct write this-->Mode=stats.mode(height)
Mode=stats.mode(a2)
print(Mode)
#so here the mode() prints the most common element whose value is minimum among most common elements(5.5 & 5.3)i.e 5.3


# In[24]:


#we can also do an experiment
#let's take a list which contains salaries of different category of employes of an organisation
salary=[4000,3500,8000,3500,5000,5000,5000]
#here 3500 occurs 2 times and 5000 occurs 3 times
#let's find out the output of mode() int his case.
Mode=stats.mode(salary)
print(Mode)
#so here it prints 5000 which is most common element in the list


# In[ ]:




