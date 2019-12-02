#!/usr/bin/env python
# coding: utf-8

# In[ ]:


command=""
while True:
    command=input(" >").lower()
    if command=="start":
        print("car is  started")
    elif command=="stop":
         print("car is  stopped")
    


# In[1]:


command=input(" >").lower()
print(command)


# In[3]:


for item in range(5):
     print (item)


# In[5]:


for item in range(1,5):
       print (item)


# In[6]:


for item in range(1,1):
       print (item)


# In[7]:


for item in range(1,2):
       print (item)


# In[8]:


for item in range(1,3):
       print (item)


# In[9]:


for item in range(1,10,2):
       print (item)


# In[11]:


for item in range(2,10,2):
       print (item)


# In[12]:


for item in range(4,1,7):
       print (item)


# In[13]:


for item in range(6,10,2):
       print (item)


# In[14]:


for item in range(1,,2):
       print (item)


# In[16]:


for item in range(1,6,0):
       print (item)


# In[17]:


for item in range(8,10):
       print (item)


# In[20]:


for x in range(3):
    for y in range(1):
        print(f"({x},{y})")


# In[37]:


rev=int(0)
no=int(123456)
s=int(0)
for i in range(0,6):
    s=int(no%10)
    rev=int(rev*10+s)
    no=int(no/10)
print("Reverse number 1234566 to",rev)     
    


# In[43]:


dec=9
bin=0
for i in range(0,4):
    s=int(dec%2)
    bin=int(bin*10+s)
    dec=int(dec/2)
print("Binary value of 9 is:",bin)


# In[78]:


binary='1001'
d=0
m=0
for i in range(0,4):
    no= binary[i]
    m= (pow(2,i)*int(no))
    d+=m
print("Binary (1001 )to decimal onversion:",d)
    
    
   


# In[88]:


print(pow(2,1))


# In[87]:


no=12345
s=0
r=0
for i in range (0,23):
    r=int(no%10)
    if no>0:
        s+=1
        no=int(no/10)
print("Length of number is",s)        


# In[69]:


a= int((pow(2,3))*1)
print(a)


# In[70]:


for i in range(0,4):
    no= binary[i]
    print(no)


# In[ ]:




