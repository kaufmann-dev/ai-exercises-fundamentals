#!/usr/bin/env python
# coding: utf-8

# # NumPy fundamentals
# 
# Many thanks to: https://numpy.org/doc/stable/user/absolute_beginners.html
# 
# ## Introduction
# 
# There are 6 general mechanisms for creating arrays:
# 
# 1. Conversion from other Python structures (i.e. lists and tuples) 
# 
# 2. Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)
# 
# 3. Replicating, joining, or mutating existing arrays
# 
# 4. Reading arrays from disk, either from standard or custom formats
# 
# 5. Creating arrays from raw bytes through the use of strings or buffers
# 
# 6. Use of special library functions (e.g. random)
# 
# In most case, we do it as described in 1 or 2.

# In[1]:


# Import numpy
import numpy as np


# ## How to create a basic array (=Vector)
# To create a NumPy array, you can use the function `np.array()`. All you need to do to create a simple array is pass a list to it.

# In[2]:


# NumPy ist jetzt über diesen alias verfügbar:
a = np.array([1,2,3])
print(a)

data = [1,2,3]
a2 = np.array(data)
print(a2)
print("Arrays sind vom Typ np.ndarray: ", type(a2))


# You can visualize your array this way:
# <img src="res/np_array.png">
# 
# ### How do we get the dimension, size or shape of an array?
# - `ndarray.ndim` will tell you the number of axes, or dimensions, of the array.
# 
# - `ndarray.size` will tell you the total number of elements of the array. This is the product of the elements of the array’s shape.
# 
# - `ndarray.shape` will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3).
# - `ndarray.dtype` will tell you the data type. The Elements are all of the same type.

# In[3]:


a.ndim


# In[4]:


a.size


# In[5]:


a.shape


# In[6]:


a.dtype


# ### Intrinsic NumPy array creation functions
# - `np.zeros()` creates an array filled with 0’s
# - `np.ones()` creates an array filled with 1’s
# - `np.arange()` creates an array with a range of elements
# - `np.linspace()` creates an array with values that are spaced linearly in a specified interval 

# In[7]:


z = np.zeros(2)
print(type(z))
print(z.ndim)
print(z.shape)

print("\n--- Matrix 2D Array ---")
z2 = np.zeros((2,2), dtype="int8")
print(z2)
print(z2.ndim)
print(z2.shape)
print(z2.dtype)


# In[8]:


help(np.zeros)
get_ipython().run_line_magic('pinfo', 'np.zeros')


# In[9]:


# Es gilt das gleiche wie bei zeros
np.ones(4)


# In[10]:


#Bei einem Wert: srop-wert
print(np.arange(10))

#Bei zwei Werten: stop -und startwert
print(np.arange(5,10))

#Bei drei Werten: stop, start, stufen
print(np.arange(5,20,2))



np.linspace(0,10,num=5).shape


# ### Specifying your data type
# While the default data type is floating point (`np.float64`), you can explicitly specify which data type you want using the `dtype` keyword.

# In[11]:


o = np.ones(2)
print(o)
print(o.dtype)


# In[12]:


#Änderung via Attribut dtype
o.dtype = "int8"
print(o.dtype)


# ### What about reshaping an array?
# Yes, this is possible, but a little tricky! 
# 
# >Using `arr.reshape()` will give a new shape to an array without changing the data. Just remember that when you use the reshape method, the array you want to produce needs to have the **same number of elements** as the original array. If you start with an array with 12 elements, you’ll need to make sure that your new array also has a total of 12 elements.

# In[13]:


hoho = np.arange(1,7)
print(hoho)
print(hoho.ndim)
print(hoho.shape)


# To reshape this vector in an array with three rows and two columns, use `reshape(3,2)`.

# In[27]:


print(hoho.reshape(2,3))


# <img src="res/np_reshape.png" width="70%">

# Eureka! We converted a vector into a 2D array (Matrix). To convert the array back to a vector, use `reshape` again

# In[28]:


print(hoho.reshape(6))


# ### Indexing and slicing
# You can index and slice NumPy arrays in the same ways you can slice Python lists.

# In[39]:


data = np.arange(10)


# In[42]:


print(data[4:9])


# <img src="res/np_indexing.png">

# ## Basic array operations
# ### Broadcasting
# There are times when you might want to carry out an operation between an array and a single number (also called an operation between a vector and a scalar). For example, your array (we’ll call it “data”) might contain information about distance in miles but you want to convert the information to kilometers. You can perform this operation with:

# In[62]:


data = np.array([1.0, 2.0])
print(data * 1.6)


# <img src="res/np_multiply_broadcasting.png">

# ### Addition, subtraction, multiplication, division, and more

# In[55]:


data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(f"data: {data}")
print(f"ones: {ones}")


# <img src="res/np_data_plus_ones.png">

# In[56]:


print(data + ones)


# In[57]:


print(data - ones)


# In[60]:


print(data * data)


# In[61]:


print(data / data)


# <img src="res/np_sub_mult_divide.png">

# ### More useful array operations

# In[64]:


ayray = np.array([1, 2, 3])


# In[65]:


print(ayray.max())


# In[66]:


print(ayray.min())


# In[67]:


print(ayray.sum())


# <img src="res/np_aggregation.png">

# ## Creating 2D arrays (matrices)
# You can pass Python lists of lists to create a 2-D array (or “matrix”) to represent them in NumPy.

# In[69]:


data = np.array([[1,2],[3,4],[5,6]])
print(data)


# <img src="res/np_create_matrix.png" width="90%">

# ### Indexing and slicing operations 

# In[70]:


print(data[0,1])


# In[71]:


print(data[1:3])


# In[72]:


print(data[0:2,0])


# <img src="res/np_matrix_indexing.png">

# ### Useful operations with matrices 

# In[73]:


print(data.max())


# In[74]:


print(data.min())


# In[75]:


print(data.sum())


# <img src="res/np_matrix_aggregation.png">

# You can aggregate all the values in a matrix and you can aggregate them across **columns** or **rows** using the `axis` parameter:

# In[79]:


data = np.array([[1,2],[5,3],[4,6]])
print(data)


# In[80]:


print(data.max(axis=0))


# In[81]:


print(data.max(axis=1))


# <img src="res/np_matrix_aggregation_row.png">

# Once you’ve created your matrices, you can add and multiply them using arithmetic operators if you have **two matrices** that are the **same size**.

# In[83]:


data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])

print(data + ones)


# <img src="res/np_matrix_arithmetic.png">

# You can do these arithmetic operations on matrices of different sizes, but only if one matrix has only one column or one row. In this case, NumPy will use its **broadcast rules** for the operation.

# In[84]:


data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])

print(data + ones_row)


# <img src="res/np_matrix_broadcasting.png">

# ### Transposing a matrix

# In[87]:


print(f"{data}\n")
print(data.transpose())


# ### Flattening multidemsional arrays

# In[91]:


print(f"{data}\n")
print(data.flatten())


# ### Dot product of two arrays

# In[90]:


a = [1, 2, 3]
b = [4, 5, 6]

print(a)
print(f"{b}\n")
print(np.dot(a, b))

