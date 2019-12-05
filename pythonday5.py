#!/usr/bin/env python
# coding: utf-8

# ##Print statements:<br>

# In[1]:


name="megha"
print("your name",name)


# In[2]:


name="megha"
print(f"your name {name}")


# **QUEUE**<br>

# In[5]:


import queue
q=queue.Queue()
q.put(5)
print(q.get())


# In[6]:


import queue
q=queue.Queue()
q.put(5)
print(q.empty())


# In[8]:



import queue
q=queue.Queue()
for i in range(5):
    q.put(i)
while not q.empty():
    print(q.get(),end= ' ' )


# **LIST**

# In[1]:


help(list)


# In[2]:


l=[45,67,77,88,99]
print(type(l))


# In[3]:


l=[45,67,77,88,99]
l.append(44)
print(l)


# In[6]:


l=[45,67,77,88,99]
l.append('asdfghjy')
print(l)


# In[7]:


l=[45,67,77,88,99]
l.append(44,87)
print(l)


# In[10]:


l=[45,67,77,88,99]
l.insert(1,'asdfghjy')
print(l)


# In[11]:


l=[45,67,77,88,99]
l.insert(5,'asdfghjy')
print(l)


# In[13]:


l=[45,67,77,88,99]
l.remove(45,77)
print(l)


# In[14]:


l=[45,67,77,88,99]
l.remove(45)
print(l)


# In[15]:


l=[45,67,77,88,99]
l.pop()
print(l)


# In[18]:


l=[45,67,77,88,99]
del l[0]
print(l)


# In[20]:


l=[45,67,77,88,99]
del l


# In[22]:


l=[45,67,77,88,99]
l.clear()
print(l)


# In[23]:


l=[45,67,77,88,99]
l2=l.copy()
print(l)
print(l2)


# In[24]:


l=[45,67,77,88,99]
l2=list(l)
print(l)
print(l2)


# In[26]:


l1=[45,67,77,88,99]
l2=['q','b','n','k','l']
l3=l1+l2
print(l3)


# In[29]:


x=0
l1=[45,67,77,88,99]
l2=['q','b','n','k','l']
for x in l2:
    l1.append(x)
print(l1)
print(l2)


# In[30]:


x=0
l1=[45,67,77,88,99]
l2=['q','b','n','k','l']
for x in l1:
    l2.append(x)
print(l1)
print(l2)


# In[35]:



l1=[45,67,77,88,99]
l2=['q','b','n','k','l']
l2.append(l1)
print(l1)
print(l2) 


# In[36]:


#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# In[43]:


l2=['q','b','n','k','l']
c=l2.count('b')
print(c)


# In[47]:


l2=['q','b','n','k','l']
l=l2.index('k')
print(l)


# 2. You need to perform accurate calculations with decimal numbers, and don’t want the small errors that naturally occur with floats;
# 
# for example, 
# a = 4.2
# b = 2.1
# a + b
# 
# (a + b) == 6.3
# 
# This is False. So, how to fix it ?

# In[58]:


a = 4.2
b = 2.1
a + b
print(round((a+b),1))
round((a + b),1) == 6.3


# In[ ]:




