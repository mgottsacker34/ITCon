# Visualizing Directors vs their Numbers of Critics

# group directors by name, and then total their numbers of critic reviews
director_critic_counts = df_copy.groupby(df_copy['director_name'])['num_critic_for_reviews'].sum()
# sort the directors based on the above value
director_critic_indx = director_critic_counts.sort_values(ascending=False)[:20].index
director_critic_values = director_critic_counts.sort_values(ascending=False)[:20].values

# define plot
fig,ax = plt.subplots(figsize=(8,6))
sns.barplot(x = director_critic_indx,
            y = director_critic_values,
            color='#90caf9',
            ax=ax)
ticks = plt.setp(ax.get_xticklabels(),rotation=90)
plt.title('Director vs critic')
plt.ylabel('Counter')
plt.xlabel('Director')
del fig,ax,ticks

#----------STOP AND PRESS SHIFT + ENTER----------
