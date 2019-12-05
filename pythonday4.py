#!/usr/bin/env python
# coding: utf-8

# In[1]:


A= 1
print(A)


# In[2]:


firstName = "meghana"

first_name="meghana"


# In[5]:


for i in range(0,5):
    if i==2:
        break
    else:
        print(i)


# In[7]:


for i in range(0,19,9):
    if i==2:
        break
    else:
        print(i)


# In[9]:


for i in range(0,5):
    if i==2:
        continue
    else:
        break
    
        
        


# In[11]:


for i in range(0,56,7):
    if i==2:
        break
    else:
        print(i)


# In[ ]:


## Python Collections (Arrays)
## There are four collection data types in the Python programming language:

## List is a collection which is ordered and changeable. Allows duplicate members.
## Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
## Set is a collection which is unordered and unindexed. No duplicate members.
## Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# In[6]:


#Reverse string
def reverse(s):
    str=" "
    for i in s:
        str=i+str
    return str


s="meghavinayaknaik"
print("Before reversing\n"+s)
print("After sting")
print(reverse(s))
    


# In[12]:


def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 

s = "Geeksforgeeks"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using recursion) is : ",end="") 
print (reverse(s))


# In[13]:


a="mm"
print(a)


# In[15]:


s="meghs"
d=(s[1:])+s[0]
print(d)


# In[21]:


s="meghs"
d=s[::-1]
print(d)


# In[22]:


s="meghs"
d=s[:-1]
print(d)


# In[23]:


s="meghs"
d=s[-1:]
print(d)


# In[27]:


s="meghsuuuuuuuuuuuuu"
d=s[1:]
print(d)


# In[ ]:


#Stacks and Queues are two key data structures often used in programming.

#A queue is a FIFO data structure: First-In First-Out in other words, it is used to implement a first come first served approach. An item that is added (enqueue) at the end of a queue will be the last one to be accessed (dequeue).

#A stack is a FILO data strucutre: First-In Last-Out. Imagine a stack of books piled up on a table. When you add (push) a book on top of the pile, it will be the first book that you will then take (pop) from the pile (stack).

#Both stacks and queues can easily be implemented in Python using a list and the append(), pop() and remove() functions.


# In[28]:


#Stack and Queues using Python - www.101computing.net/stacks-and-queues-using-python/

print(["Eric", "John", "Michael"])
print("")

queue = ["Eric", "John", "Michael"]
queue.remove(queue[0])
queue.append("Olivia")

print("> > > Queue > > >")
print(queue)
print("")


stack = ["Eric", "John", "Michael"]
stack.pop()
stack.append("Olivia")

print("> > > Stack > > >")
print(stack)


# In[30]:


# Python3 program to reverse a queue  
from queue import Queue  
  
# Utility function to print the queue  
def Print(queue): 
    while (not queue.empty()): 
        print(queue.queue[0], end = ", ")  
        queue.get() 
  
# Function to reverse the queue  
def reversequeue(queue): 
    Stack = []  
    while (not queue.empty()):  
        Stack.append(queue.queue[0])  
        queue.get() 
    while (len(Stack) != 0):  
        queue.put(Stack[-1])  
        Stack.pop() 
  
# Driver code  
if __name__ == '__main__': 
    queue = Queue() 
    queue.put('m')  
    queue.put('e')  
    queue.put('g')  
    queue.put('h')  
    queue.put('a')  
    queue.put('n')  
    queue.put('a')  
    queue.put('i')  
    queue.put('k')  
    queue.put('v')  
  
    reversequeue(queue)  
    Print(queue) 
  


# In[ ]:


#Reversing a Queue
Give an algorithm for reversing a queue Q. Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue.
dequeue() : Remove an item from front of queue.
empty() : Checks if a queue is empty or not.


# In[ ]:




