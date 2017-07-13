# Visualizing Director vs Year and Net Monetary Gain

# assign the field 'diff_gross' as the movie's gross gain minus its budget (otherwise known as Net Gain)
df['diff_gross'] = df['gross'] - df['budget']
df_copy = df.copy().dropna() #copy the data

# group the directors by name, and then add all of their Net Gains from each movie together
director_budge = df_copy.groupby(df_copy['director_name'])['diff_gross'].sum()

# sort the directors based on the above value
direcotr_budge_indx = director_budge.sort_values(ascending=False)[:20].index
# create table
director_budge_pivot = pd.pivot_table(data = df_copy[df_copy['director_name'].isin(direcotr_budge_indx)],
                                      index=['title_year'],
                                      columns=['director_name'],
                                      values=['diff_gross'],
                                      aggfunc='sum')


fig,ax = plt.subplots(figsize=(8,6))

# create heatmap
sns.heatmap(director_budge_pivot['diff_gross'],vmin=0,annot=False,linewidth=.5,ax=ax,cmap='PuBu')
plt.title('Director vs Year and diff_gross')
plt.ylabel('Year')

#----------STOP AND PRESS SHIFT + ENTER----------
