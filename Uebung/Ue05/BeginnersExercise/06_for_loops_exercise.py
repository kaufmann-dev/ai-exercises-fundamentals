#!/usr/bin/env python
# coding: utf-8

# # 1. Fill the missing pieces
# Fill the `____` parts in the code below.

# In[21]:


words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
upper_case_words = []

for x in words:
    if x.isupper():
        upper_case_words.append(x)


# In[22]:


assert upper_case_words == ['PYTHON', 'JOHN', 'DOE']


# # 2. Calculate the sum of dict values
# Calculate the sum of the values in `magic_dict` by taking only into account numeric values (hint: see [isinstance](https://docs.python.org/3/library/functions.html#isinstance)). 

# In[23]:


magic_dict = dict(val1=44, val2='secret value', val3=55.0, val4=1)


# In[36]:


# Your implementation
sum_of_values = 0
for key, value in magic_dict.items():
    if isinstance(value, (int, float)):
        sum_of_values += value
print(sum_of_values)


# In[37]:


assert sum_of_values == 100


# # 3. Create a list of strings based on a list of numbers
# The rules:
# * If the number is a multiple of five and odd, the string should be `'five odd'`
# * If the number is a multiple of five and even, the string should be `'five even'`
# * If the number is odd, the string is `'odd'`
# * If the number is even, the string is `'even'`

# In[6]:


numbers = [1, 3, 4, 6, 81, 80, 100, 95]


# In[19]:


# Your implementation
my_list = []
for x in numbers:
    if x%2:
        if x%5 == 0:
            my_list.append('five odd')
        else:
            my_list.append('odd')
    else:
        if x%5 == 0:
            my_list.append('five even')
        else:
            my_list.append('even')
print(my_list)


# In[20]:


assert my_list == ['odd', 'odd', 'even', 'even', 'odd', 'five even', 'five even', 'five odd']


# In[ ]:




