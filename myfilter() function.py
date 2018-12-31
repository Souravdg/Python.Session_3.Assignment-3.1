#!/usr/bin/env python
# coding: utf-8

# In[11]:


'''
function that filters Even numbers
'''
def chkEven(num):
    if num%2 == 0:
        return True

'''
myfilter() function similar to Python's built-in function filter()
'''
def myfilter(chkEven, lst): 
    lst1=[]
    for i in range(len(lst)):
        if(chkEven(lst[i])):
            lst1.append(lst[i])
    return lst1
    

'''
Test myfilter() function
'''
lst = range(20)
list(myfilter(chkEven,lst))

