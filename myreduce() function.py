#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
myreduce() function similar to Python's built-in function reduce()
'''
def myreduce(fn, lst):
    res = lst[0]
    for i in lst[1:]:
        res = fn(res, i)
    return res

'''
Test myreduce() function
'''
lst = [1,3,5,6]
#myreduce((lambda x, y: x * y), lst)

myreduce((lambda x, y: x + y), lst)

