
# coding: utf-8

# In[70]:


import facebook


# In[85]:


graph = facebook.GraphAPI(access_token="EAACEdEose0cBAMb0MwcDij8E9mKV7GuQy0ZAhwRUMBY0TrAY99bofQ8H1KsrRYgb68ZCptBXvslV6K0YAFXZAgnsWsoaQkLWZB70x4MLMsxuKdpzdOG7k9xxZAcSYHs4d3XFNeOoUiyhQ2b6gFqYUZBjS8DpU6tI6Tia7MHb80hCAiAQEAIsFPo90OfBMoFHDTicZCrOrOYZBAZDZD")
args = {'fields' : 'id,name,posts' }

profile = graph.get_object('Olcademy',**args)
profile


# In[30]:


type(profile)


# In[40]:


type(profile['posts'])


# In[42]:


a=profile['posts']


# In[46]:


b=a['data']
b


# In[86]:


for i in range(len(b)):
    c=b[i]
    if 'message' in c:
        d= c['message']
    print(d,end="\n\n----------------------------------------------------------------------------------------------------\n\n")

