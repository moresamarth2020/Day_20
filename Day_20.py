#!/usr/bin/env python
# coding: utf-8

# # Operations-on-Tuples
# ## Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

# In[1]:


countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)


# In[5]:


Num = (10,15,20,30,40,45,50)
temp = list(Num)
temp.append(55)
temp.pop(2)
Num = tuple(temp)
print(Num)


# Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.
# However, we can directly concatenate two tuples without converting them to list.

# In[2]:


countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


# ### Tuple methods

# As tuple is immutable type of collection of elements it have limited built in methods.They are explained below
# #### count() Method:
# The count() method of Tuple returns the number of times the given element appears in the tuple.

# In[6]:


tuple1 =(1,2,3,3,4,5,6,2,3,44,3,2,5,3)
new=tuple1.count(3)
print(new)


# In[7]:


Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)


# #### index() method
# The Index() method returns the first occurrence of the given element from the tuple.
# - #Syntax:
# tuple.index(element, start, end)

# In[9]:


Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)


# In[ ]:




