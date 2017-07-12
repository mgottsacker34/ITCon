country_gross = df_copy.groupby(df['country'])['diff_gross'].sum().sort_values(ascending=False)
country_gross_indx = country_gross[:20].index

country_pivot = pd.pivot_table(data = df_copy[df_copy['country'].isin(country_gross_indx)],
                               index=['title_year'],
                               columns=['country'],
                               values=['diff_gross'],
                               aggfunc='sum')
fig,ax = plt.subplots(figsize=(8,10))
sns.heatmap(country_pivot['diff_gross'],vmin=0,linewidth=.5,annot=False,cmap='PuBu',ax=ax)
plt.title('Country\'s diff_gross vs year')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)
del fig,ax,ticks

df_copy['critic_ratio'] = df_copy['num_critic_for_reviews'] / df_copy['num_user_for_reviews']
df_copy.head()
