#!/usr/bin/env python
# coding: utf-8

# **Difference between compiler and interpreter**

# In[ ]:


BASIS FOR COMPARISON	                        COMPILER	                                    INTERPRETER
-------------------------------------------------------------------------------------------------------------------------------------
Input	                      It takes an entire program at a time.                             It takes a single line of code                                                                                                 or instruction at a time.
Output	                      It generates intermediate object code.	                        It does not produce any                                                                                                         intermediate object code.
Working mechanism             The compilation is done before execution.	                        Compilation and execution take                                                                                                 place simultaneously.
Speed                         Comparatively faster	                                            Slower
Memory                        Memory requirement is more due to the creation of object code.	It requires less memory as it                                                                                                   does not create intermediate                                                                                                   object code.
Error                         Display all errors after compilation, all at the same time.	    Displays error of each line one                                                                                                 by one.
Error detection	              Difficult	                                                        Easier comparatively
                                        
Pertaining                    C, C++, C#, Scala, typescript uses compiler                       PHP, Perl, Python,             Programming languages                                                                           Ruby uses an                                                                                                                   interpreter.


# **HOW STRING WORKS?**

# String literals can be enclosed by either double or single quotes

# In[3]:


a="abcjdh"
b='avsjdj'
print(a,b)


# **String methods**

# 
# **s.lower(), s.upper() -- returns the lowercase or uppercase version of the string**
# 
# **s.strip() -- returns a string with whitespace removed from the start and end**
# 
# **s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes**
# 
# **s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string**
# 
# **s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found**
# 
# **s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'**
# 
# **s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.**
# 
# **s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc**

# String Slices
# The "slice" syntax is a handy way to refer to sub-parts of sequences -- typically strings and lists. The slice s[start:end] is the elements beginning at start and extending up to but not including end. Suppose we have s = "Hello"
# 
# the string 'hello' with letter indexes 0 1 2 3 4
# 
# s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4
# s[1:] is 'ello' -- omitting either index defaults to the start or end of the string
# s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
# s[1:100] is 'ello' -- an index that is too big is truncated down to the string length
# s[-1] is 'o' -- last char (1st from the end)
# s[-4] is 'e' -- 4th from the end
# s[:-3] is 'He' -- going up to but not including the last 3 chars.
# s[-3:] is 'llo' -- starting with the 3rd char from the end and extending to the end of the string.

# String built in functuins:
#     https://docs.python.org/3/library/stdtypes.html#string-methods

# In[66]:


**String Methods**

Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

Method	                     Description
capitalize()	             Converts the first character to upper case
casefold()	                 Converts string into lower case
center()	                 Returns a centered string
count()	                     Returns the number of times a specified value occurs in a string
encode()	                 Returns an encoded version of the string
endswith()	                 Returns true if the string ends with the specified value
expandtabs()	             Sets the tab size of the string
find()	                     Searches the string for a specified value and returns the position of where it was found
format()	                 Formats specified values in a string
format_map()	             Formats specified values in a string
index()	                     Searches the string for a specified value and returns the position of where it was found
isalnum()	                 Returns True if all characters in the string are alphanumeric
isalpha()	                 Returns True if all characters in the string are in the alphabet
isdecimal()	                 Returns True if all characters in the string are decimals
isdigit()	                 Returns True if all characters in the string are digits
isidentifier()	             Returns True if the string is an identifier
islower()	                 Returns True if all characters in the string are lower case
isnumeric()	                 Returns True if all characters in the string are numeric
isprintable()	             Returns True if all characters in the string are printable
isspace()	                 Returns True if all characters in the string are whitespaces
istitle()	                 Returns True if the string follows the rules of a title
isupper()	                 Returns True if all characters in the string are upper case
join()	                     Joins the elements of an iterable to the end of the string
ljust()	                     Returns a left justified version of the string
lower()	                     Converts a string into lower case
lstrip()	                 Returns a left trim version of the string
maketrans()	                 Returns a translation table to be used in translations
partition()	                 Returns a tuple where the string is parted into three parts
replace()	                 Returns a string where a specified value is replaced with a specified value
rfind()	                     Searches the string for a specified value and returns the last position of where it was found
rindex()	                 Searches the string for a specified value and returns the last position of where it was found
rjust()	                     Returns a right justified version of the string
rpartition()	             Returns a tuple where the string is parted into three parts
rsplit()	                 Splits the string at the specified separator, and returns a list
rstrip()	                 Returns a right trim version of the string
split()	                     Splits the string at the specified separator, and returns a list
splitlines()	             Splits the string at line breaks and returns a list
startswith()	             Returns true if the string starts with the specified value
strip()	                     Returns a trimmed version of the string
swapcase()	                 Swaps cases, lower case becomes upper case and vice versa
title()	                     Converts the first character of each word to upper case
translate()	                 Returns a translated string
upper()	                     Converts a string into upper case
zfill()	                     Fills the string with a specified number of 0 values at the beginning


# **The ASCII Character Set**
# 
# Character data is represented in a computer by using standardized numeric codes which have been developed. The most widely accepted code is called the American Standard Code for Information Interchange ( ASCII). The ASCII code associates an integer value for each symbol in the character set, such as letters, digits, punctuation marks, special characters, and control characters. Some implementations use other codes for representing characters, but we will use ASCII since it is the most widely used. The ASCII characters and their decimal code values are shown in Table 4.2. Of course, the internal machine representation of characters is in equivalent binary form.
# 
# **A to Z ASCII Values 65 to 90**    
# 
# **a to z ASCII Values 97 to 122**

# **Print all prime number**

# In[48]:


Start=int(input("Enter starting number: "))
End=int(input("Enter a ending number: "))
print("Prime numbers are : ",end=' ')
for i in range(Start,End):
    b=0
    for j in range(2,i):
        if i%j==0:
            b+=1
        else:
            continue
    if b>=1:
        continue
    else:
        print(i,end=' ')


# **Fibonaci number**

# In[42]:


fib1=0
fib2=1
fib3=0
print("Fibonaci numbers are",fib1,fib2,end=' ')
for i in range(0,10):
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
    print(fib2,end=' ')
    


# **Perfect Numbers**

# In[47]:


Start=int(input("Enter starting number: "))
End=int(input("Enter a ending number: "))
print("Perfect numbers are : ",end=' ')
for i in range(Start,End):
    b=0
    for j in range(1,i):
        if i%j==0:
            b+=j
        else:
            continue
    if b!=i:
        continue
    else:
        print(i,end=' ')
    

            


# **Python Collections (Arrays)**
# 
# There are four collection data types in the Python programming language:
# 
# * **List** is a collection which is ordered and changeable. Allows duplicate members.
# * **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.
# * **Set** is a collection which is unordered and unindexed. No duplicate members.
# * **Dictionary** is a collection which is unordered, changeable and indexed. No duplicate members.
# 
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a      particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
# 
# **List**
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

# In[49]:


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# In[50]:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# In[51]:


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# In[52]:


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# In[53]:


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# In[54]:


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# In[55]:


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# In[56]:


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# In[57]:


thislist = ["apple", "banana", "cherry"]
del thislist


# In[58]:


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# In[59]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# In[60]:


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# In[61]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[62]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# In[64]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# In[65]:


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# **List Methods**
# 
# **Python has a set of built-in methods that you can use on lists.**
# 
# Method	        Description
# --------------------------------------------------------------------------------------------------------------------------------
# append()	    Adds an element at the end of the list
# clear()	        Removes all the elements from the list
# copy()	        Returns a copy of the list
# count()	        Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	        Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	        Sorts the list

# **QUEUE**<br>

# **Stacks and Queues using Python**
# 
# **Stacks and Queues are two key data structures often used in programming.**
# 
# A queue is a FIFO data structure: First-In First-Out in other words, it is used to implement a first come first served approach.
# An item that is added (enqueue) at the end of a queue will be the last one to be accessed (dequeue).
# 
# A stack is a FILO data strucutre: First-In Last-Out. 
# Imagine a stack of books piled up on a table. When you add (push) a book on top of the pile, it will be the first book that you will then take (pop) from the pile (stack).

# In[71]:


print(["Eric", "John", "Michael"])

queue = ["Eric", "John", "Michael"]
queue.remove(queue[0])
queue.append("Olivia")

print("> > > Queue > > >")
print(queue)
print("")


# In[69]:


stack = ["Eric", "John", "Michael"]
stack.pop()
stack.append("Olivia")

print("> > > Stack > > >")
print(stack)


# In[74]:


# Python program to reverse a string using stack 
  
# Function to create an empty stack.  
# It initializes size of stack as 0 
def createStack(): 
    stack=[] 
    return stack 
  
# Function to determine the size of the stack 
def size(stack): 
    return len(stack) 
  
# Stack is empty if the size is 0 
def isEmpty(stack): 
    if size(stack) == 0: 
        return true 
  
# Function to add an item to stack .  
# It increases size by 1  
def push(stack,item): 
    stack.append(item) 
  
#Function to remove an item from stack.  
# It decreases size by 1 
def pop(stack): 
    if isEmpty(stack): return
    return stack.pop() 
  
# A stack based function to reverse a string 
def reverse(string): 
    n = len(string) 
      
    # Create a empty stack 
    stack = createStack() 
  
    # Push all characters of string to stack 
    for i in range(0,n,1): 
        push(stack,string[i]) 
  
    # Making the string empty since all  
    #characters are saved in stack  
    string="" 
  
    # Pop all characters of string and  
    # put them back to string 
    for i in range(0,n,1): 
        string+=pop(stack) 
          
    return string 
      
# Driver program to test above functions 
string="GeeksQuiz"
string = reverse(string) 
print("Reversed string is " + string) 
  
# This code is contributed by Sunny Karira


# In[84]:


a=[11,22,33,55,11]
b=a[0]
for i in range(0,4):
    if a[0]>a[i]:
        b=a[i]
    else:
        continue
print(b)


# In[97]:


b=0
c=0
a=[11,22,33,55,11]
for i in range(0,5):
    c=0
    for j in range(0,5):
        if a[i]==a[j]:
             c+=1
        else:
            continue
print(a[i],"is",c,"times repeated")        
    


# In[101]:


a=[122,45,45,67,89,45]
a=list(dict.fromkeys(a))
print(a)


# In[106]:


a={'name':'meg','work':'testing','name':'mega','anothername':'mega'}
print(a)


# In[110]:


a=('jon','jon','ron','hall')
print("Before converting list to set ",a)
b=set(a)
a=list(b)
print("After converting set to list",a)


# In[ ]:


a=[1,2,3,4,8,9]
for i in range(0:):
    if a[i]==a[i+1]:
        


# In[2]:


a=" anbvfg hjjj "
b=a.strip()
print(b)


# In[5]:


a="ssjdj djnjf fhfh ffff"
print(a.split())


# In[7]:


line = 'asdf fjdk; afed, fjek,asdf,      foo'
print(line.split(","))


# 1. You need to split a string into fields, but the delimiters (and spacing around them) aren’t consistent throughout the string.
# 
# input: 
# line = 'asdf fjdk; afed, fjek,asdf,      foo'
# 
# Output:
# line = 'asdf fjdk; afed, fjek,asdf,      foo'
# 

# In[9]:


line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re
re.split(r'[;,\s]\s*', line)


# 2. You need to perform accurate calculations with decimal numbers, and don’t want the small errors that naturally occur with floats;
# 
# for example, 
# a = 4.2
# b = 2.1
# a + b
# 
# (a + b) == 6.3

# In[12]:


a=4.2
b=2.1
round((a+b),1)==6.3


# In[16]:


a=4.2
b=2.1
c=a+b
print(c)
print(round((a+b),1))
round((a+b),1)==6.3


# 1. You want to round a floating-point number to a fixed number of decimal places;
# 
# input: 1.23
# output: 1

# In[17]:


a=1.23
print(round(a))


# 9. You need to format text with some sort of alignment applied
# 
# input: "hello"
# 
# output: "    hello    "

# In[18]:


a="hello"
print(a.center(20))


# In[19]:


"hello".center(20,'*')


# 8. You want to strip unwanted characters, such as whitespace, from the beginning, end, or middle of a text string.
# 
# input:
# s = '   hello world  \n'

# In[21]:


s = '   hello world  \n'
print(s.strip())


# 7. You’re working with Unicode strings, but need to make sure that all of the strings have the same underlying representation.
# 
# s1 = 'Spicy Jalape\u00f1o'
# s2 = 'Spicy Jalapen\u0303o'

# In[22]:


s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
s1=len(s1)
s2=len(s2)
if s1==s2:
    print("Both are same")
else:
    print("Both are different")


# 6. You need to search for and possibly replace text in a case-insensitive manner.
# 
# input: text = 'UPPER PYTHON, lower python, Mixed Python'
# 

# In[23]:


"python".upper()


# In[24]:


'PYTHON'.lower()


# In[25]:


"python".capitalize()


# 5. You want to search for and replace a text pattern in a string.

# In[27]:


a="Hi, Good Morning"
a.replace('Morning',"Night")


# 4. You want to match or search text for a specific pattern.
# 
# input: text = 'yeah, but no, but yeah, but no, but yeah'
# 

# In[36]:


text = 'yeah, but no, but yeah, but no, but yeah'
text.find("but",15)


# Finding missing elements in list

# In[37]:


# Python3 code to demonstrate 
# Finding missing elements in List 
# using list comprehension 
  
# initializing list 
test_list = [3, 5, 6, 8, 10] 
  
# printing original list 
print("The original list : " + str(test_list)) 
  
# using list comprehension 
# Finding missing elements in List 
res = [ele for ele in range(max(test_list)+1) if ele not in test_list] 
  
# print result 
print("The list of missing elements : " + str(res))


# In[39]:


l1=[10,29,56]
l2=[12,10,25]
print(l1+l2)


# In[ ]:




