#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# In[2]:


diabetes_df = pd.read_csv("archive/diabetes.csv")
diabetes_df.describe()


# In[3]:


diabetes_df.isnull().sum()


# In[4]:


diabetes_df.head()


# In[5]:


diabetes_df.Glucose.median()


# In[6]:


X = diabetes_df
y = X.pop("Outcome")


# In[7]:


train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.3, random_state=1)


# In[8]:


X.head()


# <h2>RFC</h2>

# In[9]:


rfc_model = RandomForestClassifier(n_estimators=100, random_state=10)
rfc_model.fit(train_X, train_y)
y_pred = rfc_model.predict(val_X)
accuracy_score(val_y ,y_pred)


# <h2>Logistic Regression</h2>

# In[10]:


lr_model = LogisticRegression(C=0.8, random_state=3, solver='liblinear')
lr_model.fit(train_X, train_y)
y_pred = lr_model.predict(val_X)
accuracy_score(val_y, y_pred)


# <h2>'0' Werte ersetzen</h2>

# In[11]:


diabetes_df = pd.read_csv("archive/diabetes.csv")
diabetes_df.head()


# In[12]:


diabetes_df.groupby(['Outcome']).median()


# In[13]:


for col in diabetes_df.columns:
    print(str(col) + ": " + str(diabetes_df[col][(diabetes_df[col] == 0)].count()))


# <h3>Werte die man behandeln muss/ein Problem darstellen:</h3>
# <ul>
#     <li>Glucose</li>
#     <li>Blood Pressure</li>
#     <li>Skin Thickness</li>
#     <li>Insulin</li>
#     <li>BMI</li>
# </ul>

# In[14]:


med = diabetes_df.groupby('Outcome').Glucose.median()
med[1]


# In[15]:


diabetes_df['Glucose'] = diabetes_df.apply(lambda x: (med[0] if x['Outcome'] == 0 else med[1]) if x['Glucose'] == 0 else x['Glucose'], axis=1)
diabetes_df


# In[16]:


def replace_median(col):
    diabetes_df[col] = diabetes_df.apply(lambda x: (med[0] if x['Outcome'] == 0 else med[1]) if x[col] == 0 else x[col], axis=1)

replace_median("BloodPressure")
replace_median("SkinThickness")
replace_median("Insulin")
replace_median("BMI")


# In[17]:


for col in diabetes_df.columns:
    print(str(col) + ": " + str(diabetes_df[col][(diabetes_df[col] == 0)].count()))


# In[18]:


X = diabetes_df
y = X.pop("Outcome")


# In[19]:


train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.3, random_state=7)


# <h2>Random Forest</h2>

# In[20]:


rfc_model = RandomForestClassifier(n_estimators=110, random_state=9)
rfc_model.fit(train_X, train_y)
y_pred = rfc_model.predict(val_X)
accuracy_score(val_y ,y_pred)


# <h2>Logistic Regression</h2>

# In[41]:


lr_model = LogisticRegression(C=1, random_state=10, solver='liblinear')
lr_model.fit(train_X, train_y)
y_pred = lr_model.predict(val_X)
accuracy_score(val_y, y_pred)
