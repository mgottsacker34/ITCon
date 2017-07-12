import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

director_critic_ratio = df_copy.groupby(df_copy['director_name'])['critic_ratio'].mean()
director_critic_idx =director_critic_ratio.sort_values(ascending=False)[:20].index
director_critic_val =director_critic_ratio.sort_values(ascending=False)[:20].values

director_critic_pivot = pd.pivot_table(data=df_copy[df_copy['director_name'].isin(director_critic_idx)],
                                       index=['title_year'],
                                       columns=['director_name'],
                                       values=['critic_ratio'],
                                       aggfunc='mean')
fig,ax = plt.subplots(figsize=(8,10))
sns.heatmap(director_critic_pivot['critic_ratio'],vmin=0,annot=False,linewidth=.5,ax=ax)
plt.title('Top 20 critic ratio')
plt.ylabel('Year')
plt.xlabel('Director')
