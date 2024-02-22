#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install gensim==3.6.0')


# In[16]:


from gensim.summarization import summarize

# This is your text
text = """
Romeo and Juliet is a tragedy written by William Shakespeare early in his career about two young star-crossed lovers whose deaths ultimately reconcile their feuding families. It was among Shakespeare's most popular plays during his lifetime and along with Hamlet, is one of his most frequently performed plays. Today, the title characters are regarded as archetypal young lovers.
"""

# Summarize the text
summary = summarize(text, ratio=0.5)


print(summary)


# In[17]:


# Evaluation with Rouge
rouge = Rouge()

scores = rouge.get_scores(summary, text)

print("\nRouge Scores:")
print(scores)


# In[ ]:




