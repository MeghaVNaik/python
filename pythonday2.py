#!/usr/bin/env python
# coding: utf-8

# In[1]:


course= "python for beginners"
print(course[0:7])


# In[2]:


course= "python for beginners"
print(course[0:-5])


# In[3]:


course= "python for beginners"
print(course[:-5])


# In[4]:


course= "python for beginners"
print(course[0:])


# In[5]:


course= "python for beginners"
print(course[-3:])


# In[6]:


is_hot=True
is_cold=False
if is_hot:
      print("Its hot day")
elif is_cold:
      print("Its cold day")
else:
     print("Its lovely day")

print("Enjoy your day")


# In[8]:


has_good_credit= True
has_criminal_record=False
if has_good_credit and not has_criminal_record:
    print("ELIGIBLE")


# In[11]:


name= input("Enter your name ")
length= len(name)
if length<3:
   print("Name must be at least 3 charcters")
elif length>50:
   print("Name must be less than or equal to 50 charcters")
else:
   print("Name looks good!")


# In[17]:


i=1
while i<=5:
    print(i)
    i=i+1
print("done")


# In[2]:


i=1
while i<=6:
    print('*'*i)
    i+=1
    
    


# In[3]:


guess=9
for i in range(3):
    guessn=int(input("guess "))
    if guessn==guess:
        print("your are correct")
        break
    else:
        print("Your are wrong")
        


# In[4]:


names=['john','nancy','mosh','sara']
print(names[-1])


# In[5]:


names=['john','nancy','mosh','sara']
print(names[2])


# In[1]:


names=['john','nancy','mosh','sara']
print(names[2:6])


# In[2]:


names=['john','nancy','mosh','sara']
print(names[2:-3])


# In[3]:


names=['john','nancy','mosh','sara','magi','gigi','megi']
print(names[2:-3])


# In[6]:


multi = """It was the best of times.
  It was the worst of times."""
print (multi)


# In[7]:


multi = """It was the best of times.
  It was the worst of times."""
print (multi[8:9])


# In[9]:


multi = """It was the best of times.
  It was the worst of times."""
print (multi[14:56])


# In[10]:


multi = """It was the best of times.
  It was the worst of times."""
print (multi[-56:-1])


# In[11]:


multi = """It was the best of times.
  It was the worst of times."""
print (multi[-5:-1])


# In[25]:


speed=228
if speed >= 80: 
    print ('You are so busted')
else:
    print ('Have a nice day')


# In[ ]:




