#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None



# Now we need to read in the data
df = pd.read_csv(r'C:\Users\dh212182\OneDrive - Dunnhumby Ltd\Desktop\Projects\movies.csv')


# In[3]:


df


# In[4]:


for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[30]:


df1 = df.dropna()

df1


# In[6]:


for col in df1.columns:
    pct_missing = np.mean(df1[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[7]:


df1.dtypes


# In[9]:


df1['budget'] = df1['budget'].astype('int64')
df1['gross'] = df1['gross'].astype('int64')


# In[8]:


df1['released']=df1['released'].astype('str').str[:4]


# In[10]:


pd.set_option('display.max_rows',None)


# In[31]:


df.sort_values(by=['gross'],inplace = False,ascending = False)


# In[12]:


df1.drop_duplicates()


# In[18]:


sns.regplot(x="gross", y="budget", data=df1,scatter_kws = {'color': 'red'},line_kws = {'color' : 'blue'})


# In[17]:


df1.corr(method ='pearson')


# In[19]:


df1.corr(method ='kendall')


# In[20]:


df.corr(method ='spearman')


# In[21]:


correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[22]:


df_numerized = df1


for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name]= df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes
        
df_numerized


# In[23]:


correlation_matrix = df_numerized.corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Movies")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[26]:


correlation_mat = df_numerized.corr()

corr_pairs = correlation_mat.unstack()

print(corr_pairs)


# In[27]:


sorted_pairs = corr_pairs.sort_values(kind="quicksort")

print(sorted_pairs)


# In[28]:


strong_pairs = sorted_pairs[abs(sorted_pairs) > 0.5]

print(strong_pairs)


# In[32]:


# Looking at the top 15 compaies by gross revenue

CompanyGrossSum = df1.groupby('company')[["gross"]].sum()

CompanyGrossSumSorted = CompanyGrossSum.sort_values('gross', ascending = False)[:15]

CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64') 

CompanyGrossSumSorted


# In[34]:


CompanyGrossSum = df1.groupby(['company', 'year'])[["gross"]].sum()

CompanyGrossSumSorted = CompanyGrossSum.sort_values(['gross','company','year'], ascending = False)[:15]

CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64') 

CompanyGrossSumSorted


# In[ ]:




