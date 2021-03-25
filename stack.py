#!/usr/bin/env python
# coding: utf-8

# # using_list

# In[1]:


st=[]
st.append(10)
st.append(20)
st.append(30)
st


# In[2]:


st.pop()


# In[3]:


st.pop()


# In[4]:


st.pop()


# In[5]:


st.pop()


# In[6]:


len(st)==0 #empystack


# In[7]:


not st #emptystack


# In[8]:


st.append(10)
st.append(20)
st.append(30)
st[-1] # top element


# In[10]:


stack=[]
def push():
    el=input()
    stack.append(el)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)
while True:
    print("select operration press 1. Push 2. Pop 3.Exit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("please enter the correct operation")


# In[11]:


stack=[]
def push():
    if len(stack)==a:
        print("list is full")
    else:
        el=input()
        stack.append(el)
        print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)
a=int(input("enter limit of stack"))
while True:
    print("select operration press 1. Push 2. Pop 3.Exit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("please enter the correct operation")


# # using_modules 

# In[12]:


import collections


# In[19]:


stack=collections.deque()
type(stack)


# In[20]:


stack.append(10)
stack.append(20)
stack.append(30)


# In[21]:


stack


# In[22]:


stack.pop()


# In[23]:


stack.pop()


# In[24]:


stack.pop()


# In[25]:


stack.pop()


# In[27]:


not stack


# In[28]:


stack.append(10)
stack.append(20)


# In[29]:


stack[-1]


# In[1]:


import queue


# In[2]:


stack=queue.LifoQueue()


# In[32]:


stack.put(10)
stack.put(20)


# In[33]:


stack.get()


# In[34]:


stack.get()


# In[ ]:


stack.get() #its take time becuase stack is empty 


# In[2]:


stack=queue.LifoQueue(3) #limit of stack


# In[3]:


stack.put(10)
stack.put(20)
stack.put(30)


# In[4]:


stack.put(40,timeout=1)


# In[5]:


stack.get()


# In[6]:


stack.get()


# In[7]:


stack.get()


# In[8]:


stack.get(timeout=1)


# In[ ]:




