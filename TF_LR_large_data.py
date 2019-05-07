#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


import tensorflow as tf


# In[3]:


x_data = np.linspace(0.0,10.0,1000000)


# In[4]:


noise = np.random.randn(len(x_data))


# In[5]:


noise


# In[6]:


y_true = (0.5 * x_data) + 5 + noise


# In[7]:


x_df = pd.DataFrame(data = x_data,columns=['X Data'])


# In[8]:


y_df = pd.DataFrame(data = y_true,columns=['Y'])


# In[9]:


y_df.head()


# In[10]:


my_data = pd.concat([x_df,y_df],axis=1)


# In[11]:


my_data.head()


# In[12]:


my_data.sample(n=250).plot(kind='scatter',x='X Data',y='Y')


# In[13]:


batch_size = 8
np.random.randn(2)


# In[14]:


m = tf.Variable(-1.38274668)
b = tf.Variable(-0.50337975)


# In[15]:


xph = tf.placeholder(tf.float32,[batch_size])
yph = tf.placeholder(tf.float32,[batch_size])


# In[16]:


y_model = m*xph + b


# In[17]:


error = tf.reduce_sum(tf.square(yph - y_model))


# In[18]:


optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.001)
train = optimizer.minimize(error)


# In[19]:


init = tf.global_variables_initializer()


# In[24]:


with tf.Session() as sess:
    sess.run(init)
    batches = 100
    for i in range(batches):
        rand_ind = np.random.randint(len(x_data),size = batch_size)
        feed = {xph:x_data[rand_ind],yph:y_true[rand_ind]}
        sess.run(train,feed_dict = feed)
        model_m, model_b = sess.run([m,b])
        y_hat = x_data*model_m + model_b
        plt.clf()
        my_data.sample(n=250).plot(kind='scatter',x='X Data',y='Y')
        plt.plot(x_data,y_hat,'r')
# In[21]:


model_m


# In[22]:


model_b


# In[25]:





# In[ ]:




