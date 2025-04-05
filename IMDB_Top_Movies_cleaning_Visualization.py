#!/usr/bin/env python
# coding: utf-8

# In[162]:


import pandas as pd
import numpy as np 
df = pd.read_csv("IMDB_Top_Movies.csv")
df.head()


# In[163]:


df.tail()


# In[164]:


# Remove rows where Title is 'Not Found'
df = df[df['Title'] != 'Not Found']


# In[165]:


print(df.columns)         


# In[166]:


print(df.shape)           


# In[167]:


print(df.info())


# In[168]:


print(df.isnull().sum())


# In[159]:


df.replace("Not Found", np.nan, inplace=True)


# In[169]:


df['Director'] = df['Director'].fillna("Unknown")
df['Genre'] = df['Genre'].fillna("Unknown")


# In[170]:


print(df.isnull().sum())


# In[171]:


# Convert to lowercase
df['Genre'] = df['Genre'].str.lower()

# Remove extra spaces
df['Genre'] = df['Genre'].str.strip()

# Replace similar words
df['Genre'] = df['Genre'].str.replace("sci-fi", "science fiction")


# In[ ]:





# In[172]:


print(df.isnull().sum())


# In[173]:


df['Description'] = df['Description'].fillna("Description not available")


# In[174]:


df['Total Ratings'] = df['Total Ratings'].str.replace('(', '', regex=False)
df['Total Ratings'] = df['Total Ratings'].str.replace(')', '', regex=False)


# In[175]:


df['Total Ratings'] = df['Total Ratings'].str.strip()


# In[176]:


df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')


# In[177]:


print(df.isnull().sum())


# In[180]:


# First, convert 'Rating' column to numeric (in case it's still string)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Calculate the mean of non-null ratings
mean_rating = df['Rating'].mean()

# Fill NaN values in 'Rating' with the mean
df['Rating'].fillna(mean_rating, inplace=True)


# In[ ]:





# In[181]:


df['Title'] = df['Title'].str.replace(r'^\d+\.\s*', '', regex=True)
print(df['Title'].head())


# In[182]:


df.to_csv("IMDB_Top_Movies_Cleaned_original.csv", index=False)


# In[183]:


import seaborn as sns
import matplotlib.pyplot as plt

# Barplot of Top 10 Ratings
top10 = df.sort_values(by='Rating', ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x='Rating', y='Title', data=top10)
plt.title("Top 10 Rated IMDB Movies")
plt.show()


# In[184]:


# Explode multiple genres
import matplotlib.pyplot as plt
import seaborn as sns

# Explode genres
df_exploded = df.assign(Genre=df['Genre'].str.split(', ')).explode('Genre')
genre_counts = df_exploded['Genre'].value_counts().head(10)

# Plot with small visual changes
plt.figure(figsize=(8, 5))
genre_counts.plot(kind='barh', color='blue', edgecolor='black')

plt.title('Top 10 Genres', fontsize=14)
plt.xlabel('Count')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()



# In[185]:


# Ratings Distribution
sns.histplot(df['Rating'], bins=10, kde=True)


# In[186]:


# Average Rating per Genre
avg_genre = df_exploded.groupby('Genre')['Rating'].mean().sort_values(ascending=False).head(10)
avg_genre.plot(kind='bar', title='Average Rating by Genre')




# In[187]:


# Director with Most Movies in Top 250
df['Director'].value_counts().head(10).plot(kind='bar', title='Top 10 Directors')


# In[188]:


df.info()


# In[ ]:





# In[ ]:




