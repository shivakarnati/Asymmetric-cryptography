#!/usr/bin/env python
# coding: utf-8

# In[21]:



get_ipython().run_line_magic('load_ext', 'sage')
reset()


# In[22]:



## generate safe prime p = 2q+1 

q_bits = 256
q = random_prime(2^(q_bits-1), 2^q_bits) ## generating random prime numbers

while not is_prime(2*q+1):               ## is 2* q+1 prime?
    q = next_prime(q)                    ## q = next_prime(q), sophie germain prime*
    
p = 2*q+1                               ## safe prime                      

print 'p =',p
print 'q =',q

## find generator g of a prime number
h = mod(primitive_root(p), p) # generator of p
g = h^2                       

# for demonstration purposes, 
# pick a large generator to make it clear that the discrete log is not trivial
g = g^(10000)
print 'g =',g


# In[24]:


## pick a at random and compute x = g^a
a = randint(1,q)
x = g^a
print 'a =',a
print 'x =',x

## pick b at random and compute y = g^b
b = randint(1,q)
y = g^b
print
print 'b =',b
print 'y =',y

## let's verify that the shared keys match
#print
print 'shared keys:'
print y^a
print x^b
print 'do both keys match?', y^a==x^b


# In[ ]:




