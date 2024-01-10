#!/usr/bin/env python
# coding: utf-8

# In[1]:


#NUMPY
#Numpy is a fundamental Python library for numerical computing that provides support for arrays, matrices, and mathematical functions to operate on these data structures. 
import numpy as np


# In[2]:


arr1=np.array([])
arr1


# In[3]:


my_list=[2,3,4,5]
print(my_list)
print(type(my_list))


# In[4]:


a=np.array(my_list)
a


# In[5]:


#nd= dimension of data
type(a)


# In[6]:


a.ndim


# In[7]:


#size isIn NumPy, the size function returns the total number of elements in an array. 
a.size


# In[8]:


#shape(In NumPy, the shape attribute of an array returns a tuple representing the shape or dimensions of the array. )

a.shape


# In[9]:


my_matrix=[[2,3,4],[5,6,7],[8,9,10]]
my_matrix


# In[10]:


b=np.array(my_matrix)
b


# In[11]:


b.ndim


# In[12]:


b.shape


# In[13]:


b.size


# In[14]:


arr1=np.array([[[11,12,13],[14,15,16]],[[17,18,19],[20,21,22]]])
arr1


# In[15]:


arr1.size


# In[16]:


arr1.shape


# In[17]:


arr1.ndim


# In[18]:


#reshape
arr1


# In[19]:


arr2=arr1.reshape((1,4,3))


# In[20]:


arr2


# In[22]:


arr2=arr1.reshape((1,3,4))


# In[23]:


arr2


# In[24]:


np.arange(20)


# In[26]:


np.arange(10,1,-3)


# In[27]:


np.arange(-20,2,4)


# In[ ]:




