
# coding: utf-8

# In[3]:


import sys
S = input().strip()
try:
    i = int(S)
    print(i)
except ValueError:
    print("Bad String")

