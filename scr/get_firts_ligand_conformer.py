#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, sys 


# In[7]:

my_files = open(sys.argv[1]).readlines() 

#my_files = open("../files/ligand_vina_out_CHEMBL126.pdbqt").readlines() 


# In[44]:


start , end  = 0,0 
counter = 0 

for num,x in enumerate( my_files):
    if  x == "MODEL 1\n"  :
        start = num 

    if "ENDMDL\n" in x: 
        if counter == 0 : 
            end = num 
            counter +=1 
        else : 
            break


# In[50]:


model = [ x.strip() for x in my_files[start:end] if x[0:4] == "ATOM" ]


# In[52]:

for x in model:
    print ( x ) 


# In[ ]:




