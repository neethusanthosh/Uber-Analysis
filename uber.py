#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv("D:/decoder lectures/casestudy/Uber Request Data.csv")
df


# In[5]:


df.head()


# In[6]:


len(df["Request id"].unique())


# In[7]:


df.shape


# In[8]:


df.isnull().sum()


# In[9]:


df.isnull().sum()/df.shape[0]*100


# In[10]:


df.info()


# In[11]:


df["Request timestamp"].value_counts()


# In[12]:


df["Request timestamp"]=df["Request timestamp"].astype(str)


# In[13]:


df["Request timestamp"]=df["Request timestamp"].replace("/","-")


# In[19]:


df["Request timestamp"]=pd.to_datetime(df["Request timestamp"],dayfirst=True)


# In[15]:


df.info()


# In[16]:


df["Drop timestamp"]=pd.to_datetime(df["Drop timestamp"],dayfirst=True)


# In[17]:


df.info()


# In[18]:


df["Drop timestamp"]


# In[20]:


req_hour=df["Request timestamp"].dt.hour


# In[21]:


len(req_hour)


# In[64]:


df["req_hour"]=req_hour
df


# In[23]:


req_day=df["Request timestamp"].dt.day


# In[65]:


df["req_day"]=req_day
df


# In[25]:


import  seaborn as sns


# In[27]:


import matplotlib.pyplot as plt


# In[28]:


sns.countplot(x="req_hour",data=df,hue="Status")
plt.show()


# In[66]:


sns.catplot(x="req_hour",data=df,row="req_day",hue="Status",kind="count")
plt.show()


# In[67]:


sns.catplot(x="req_hour",data=df,row="req_day",hue="Pickup point",kind="count")
plt.show()


# In[68]:


sns.catplot(x="req_hour",data=df,hue="Pickup point",kind="count")
plt.show()


# In[32]:


df


# In[33]:


df["Time_Slot"]=0


# In[ ]:


### 5           "Pre_morning"
5<=x<10   == "Morning Rush"
10<=x<17     'Day_time'
17<=x<22     "Evening rush"
else         "Late night"###


# In[35]:


j=0
for i in df["req_hour"]:
    if df.iloc[j,6]<5:
        df.iloc[j,8]="Pre_Morning"
    elif 5<=df.iloc[j,6]<10:
        df.iloc[j,8]="Morning_Rush"
        
    elif 10<=df.iloc[j,6]<17:
        df.iloc[j,8]="Day_Time"
        
    elif 17<=df.iloc[j,6]<22:
        df.iloc[j,8]="Evening_Rush"
    else:
        df.iloc[j,8]="Late_Night"
    j=j+1


# In[34]:


df


# In[39]:


df


# In[40]:


df["Time_Slot"].value_counts()


# In[41]:


plt.figure(figsize=(10,6))
sns.countplot(x="Time_Slot",hue="Status",data=df)
plt.show()


# In[42]:


df_morning_rush=df[df['Time_Slot']=='Morning_Rush']


# In[43]:


sns.countplot(x="Pickup point",hue="Status",data=df_morning_rush)


# In[ ]:


#severity of problem(cancellation ofcab asper pickup location)


# In[72]:


df_airport_cancelled=df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport") & (df_morning_rush["Status"]=="Cancelled")]


# In[74]:


df_airport_cancelled.shape[0]


# In[45]:


df_city_cancelled=df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City") & (df_morning_rush["Status"]=="Cancelled")]


# In[46]:


df_city_cancelled.shape[0]


# In[ ]:


#supply and demand


# In[47]:


df_morning_rush


# In[48]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City")].shape[0]


# In[49]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="City") & (df_morning_rush["Status"]=="Trip Completed")].shape[0]


# In[50]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport")].shape[0]


# In[51]:


df_morning_rush.loc[(df_morning_rush["Pickup point"]=="Airport") & (df_morning_rush["Status"]=="Trip Completed")].shape[0]


# In[52]:


#supply and demand for evening rush


# In[53]:


df_evening_rush=df[df['Time_Slot']=='Evening_Rush']


# In[54]:


df_city_cancelled=df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City") & (df_evening_rush["Status"]=="Cancelled")]


# In[55]:


sns.countplot(x="Pickup point",hue="Status",data=df_evening_rush)


# In[56]:


df_city_cancelled.shape[0]


# In[57]:


df_evening_rush["Status"].value_counts()


# In[58]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City")].shape[0]


# In[59]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City") & (df_evening_rush["Status"]=="Trip Completed")].shape[0]


# In[60]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="Airport")].shape[0]


# In[61]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="Airport") & (df_evening_rush["Status"]=="Trip Completed")].shape[0]


# In[ ]:


#problem at each location by looking at cancellation


# In[62]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="Airport") & (df_evening_rush["Status"]=="Cancelled")].shape[0]


# In[63]:


df_evening_rush.loc[(df_evening_rush["Pickup point"]=="City") & (df_evening_rush["Status"]=="Cancelled")].shape[0]


# In[76]:


#pie chart


# In[83]:


df_morning_city=df.loc[(df["Pickup point"]=="City")&(df["Time_Slot"]=="Morning_Rush")]


# In[85]:


df_morning_city_count=pd.DataFrame(df_morning_city["Status"].value_counts())


# In[86]:


df_morning_city_count


# In[87]:


df_morning_city_count["Status"].values


# In[88]:


df_morning_city_count["Status"].index


# In[90]:


fig,ax=plt.subplots()
ax.pie(df_morning_city_count["Status"].values,labels=df_morning_city_count["Status"].index)
plt.show()


# In[91]:


df_evening_airport=df.loc[(df["Pickup point"]=="City")&(df["Time_Slot"]=="Evening_Rush")]


# In[94]:


df_evening_airport_count=pd.DataFrame(df_evening_airport["Status"].value_counts())


# In[95]:


df_evening_airport_count


# In[96]:


df_evening_airport_count["Status"].values


# In[97]:


df_evening_airport_count["Status"].index


# In[98]:


fig,ax=plt.subplots()
ax.pie(df_evening_airport_count["Status"].values,labels=df_evening_airport_count["Status"].index)
plt.show()


# In[ ]:


#Recommendations
#1.They could be given bonus for each trip they complete from the city to the airport in the morning rush time. This will ensure 
#that less number of trips are cancelled.
# 2.Driver can again be given bonus to complete a trip from the airport in the evening. This will ensure that the 
#supply increase at the airport
#3. Uber can also pay driver to come without passenger to the airport.


# In[ ]:




