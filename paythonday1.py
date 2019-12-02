#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=1
print(a)


# In[4]:


a=1
s="megha"
b= True
c=11.33
f=33.0
print(a,s,b,c,f)


# In[8]:


full_name='megha'
age= 22
is_new= True
print("hi "+ full_name)
print("you are", age)


# In[11]:


name= input("Enter your name ")
print("hi "+ name)


# In[12]:


name= input("what is youtr name? ")
color= input("which is your fav color? ")
print(f'{name} likes {color}')


# In[13]:


course= "python for beginners"
print(course[2:7])


# In[21]:


fib1=0
fib2=1
fib3=0
no=10
count=0
while count<no:
    print(fib1)
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
    count+=1


# In[24]:


fib1=0
fib2=1
fib3=0
for i in range(10):
    print(fib1)
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
    
    
    


# In[27]:


for no in range(10):
    if no % 2==0:
          print(no)
  
    


# In[26]:


for no in range(10):
    if no%2==1:
        print(no)


# In[4]:


rev=0
a=0
no=int(input("Enter a number "))

a= no % 10
rev= rev * 10 +  a
no= no / 10
print("Reverse number",rev)


# In[2]:


b=0
nu=int(input("Enter a number  "))
for a in range(2,nu):
        if nu % a==0:
            b+=1
        else:
            print(nu, "is not divided by", a)
if b>=1:
    print("Its not a prime")
else:
    print("Its a prime")
    
            


# In[1]:


b=0
nu=int(input("Enter a number "))
for a in range(1,nu):
        if nu % a==0:
            b+=a
        else:
            print("fail")
if b==nu:
    print("Its a perfect number")
else:
    print("Its not a perfect number")
            
            
            


# In[ ]:


print("hi")


# In[8]:


no=123456
print(chr(no))


# In[10]:


no=234
print(chr(no))


# In[11]:


print(ord('@'))


# In[12]:


print(ord('#'))


# In[13]:


print(ord('#'))


# In[14]:


print(str('#'))


# In[15]:


print(str('a'))


# In[16]:


print(str(90))


# In[17]:


print(str('90'))


# In[18]:


s="Hi Megha"
print(s.replace('M','G'))


# In[19]:


s="himegha"
print(s.capitalize())


# In[20]:


s="HIMEGHA"
print(s.lower())


# In[21]:


s="himegha"
print(s.upper())


# In[22]:


s="HiMeGha"
print(s.swapcase())


# In[24]:


s="hi megha how are you"
print(s.title())


# In[25]:


s="hii jii hii"
print(s.count('ii'))


# In[29]:


s="hii jii hii"
print(s.count('ii',3,-1))


# In[31]:


s="hii jii hii"
print(s.endswith('ii'))


# In[32]:


s="hii jii hii"
print(s.endswith('ii',0,6))


# In[33]:


s="hii jii hii"
print(s.find('ii'))


# In[35]:


s="hii jii hii"
print(s.find('ii',2,8))


# In[36]:


s="hii jii hii"
print(s.find('s'))


# In[38]:


s="hii jii hii"
print(s.index('i',0,6))


# In[39]:


s="hii jii hii"
print(s.rfind('i',0,10))


# In[41]:


s="hii jii hii"
print(s.rindex('i',0,11))


# In[42]:


s="hii jii hii"
print(s.startswith('hi'))


# In[43]:


s="hii jii hii"
print(s.startswith('hi',8,10))


# In[45]:


s="abc1235gh"
print(s.isalnum())


# In[46]:


s="abc1235gh"
print(s.isalpha())


# In[47]:


s="abcgh"
print(s.isalpha())


# In[48]:


s="abcgh"
print(s.isdigit())


# In[49]:


s="1344"
print(s.isdigit())


# In[50]:


s="1344"
print(s.isidentifier())


# In[51]:


s="var443"
print(s.isidentifier())


# In[52]:


s="var#443"
print(s.isidentifier())


# In[53]:


s="var"
print(s.islower())


# In[54]:


"yuguh".isprintable()


# In[55]:


"yuguh\t".isprintable()


# In[56]:


'      '.isprintable()


# In[57]:


'hh nnj hj'.isspace()


# In[58]:


'hhnnjhj'.isspace()


# In[59]:


'             '.isspace()


# In[60]:


'This Is Megha'.istitle()


# In[61]:


'This is Megha'.istitle()


# In[62]:


'This is Megha'.isupper()


# In[70]:


"megha".center(15)


# In[71]:


"megha".center(15,'*')


# In[75]:


"a\tbbb\tccc".expandtabs(6)


# In[79]:


"Megha".ljust(10,"#")


# In[80]:


"               Megha             ".lstrip()


# In[81]:


"Megha".replace("e","g")


# In[82]:


"Meghana".replace("a","g",2)


# In[83]:


"Megha".rjust(10,"#")


# In[84]:


"           Megha              ".rstrip()


# In[86]:


"      hi how are you     ".strip()


# In[88]:


'ssssss'.zfill(8)


# In[89]:


','.join(['a','b','c'])


# In[90]:


"hellohihowareyou".partition("h")


# In[91]:


"hellohihowareyou".rpartition("h")


# In[93]:


"hellohihowareyou".partition("h")


# In[94]:


"hellohihowareyou".rsplit("h")


# In[95]:


'www.realpython.com'.rsplit(sep='.', maxsplit=1)


# In[96]:


'www.realpython.com'.split('.', maxsplit=1)


# In[97]:


'www.realpython.com'.rsplit('.', maxsplit=1)


# In[98]:


'foo\nbar\r\nbaz\fqux\u2028quux'.splitlines()


# In[ ]:




