#!/usr/bin/env python
# coding: utf-8

# # 1. Super vowels
# Implement `super_vowels` function which takes a string as an argument and returns a modified version of that string. In the return value of `super_vowels`, all vowels should be in upper case whereas all consonants should be in lower case. The vowels are listed in the `VOWELS` variable.

# In[3]:


VOWELS = ['a', 'e', 'i', 'o', 'u']


# In[14]:


# Your implementation here
def super_vowels(string):
    super = ''
    for x in string:
        if x.lower() in VOWELS:
            super = super + x.upper()
        else:
            super = super + x.lower()
    print(super)
    return super


# In[15]:


assert super_vowels('hi wassup!') == 'hI wAssUp!'
assert super_vowels('HOw aRE You?') == 'hOw ArE yOU?'


# # 2. Playing board
# Implement `get_playing_board` function which takes an integer as an argument. The function should return a string which resemples a playing board (e.g. a chess board). The board should contain as many rows and columns as requested by the interger argument. See the cell below for examples of desired behavior.
# 

# In[33]:


# Your implementation here
def get_playing_board(x):
    board = ''
    for i in range(x):
        for c in range(x):
            if i%2:
                if c%2:
                    board+=' '
                else:
                    board+='*'
            else:
                if c%2:
                    board+='*'
                else:
                    board+=' '
        board+='\n'
    return board


# In[34]:


board_of_5 = (
' * * \n'
'* * *\n'
' * * \n'
'* * *\n'
' * * \n'
)

board_of_10 = (
' * * * * *\n'
'* * * * * \n'
' * * * * *\n'
'* * * * * \n'
' * * * * *\n'
'* * * * * \n'
' * * * * *\n'
'* * * * * \n'
' * * * * *\n'
'* * * * * \n'
)

assert get_playing_board(5) == board_of_5
assert get_playing_board(10) == board_of_10

print(get_playing_board(50))


# In[ ]:




