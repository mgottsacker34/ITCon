# Visualizing the most popular genres across all movies

# process the data's genres.  When a movie falls into more than one genre, they are delimited with a |
movie_genres = df_copy['genres'].map(lambda x:x.split('|'))

# create array of the genres
genres = []
for genre in movie_genres:
    if(len(genre) >= 2):
        for i in genre:
            if i not in genres:
                genres.append(i)
    elif genre not in genres:
        if isinstance(genre,list):
            genres.append(genre[0])
genres = set(genres)


# process list of genres
def process_genre(genres):
    genre_list = []
    for genre in genres.split('|'):
        genre_list.append(genre)
    return genre_list
df_copy['genre_list'] = df_copy['genres'].map(process_genre)
df_copy.head()


# process genre totals
df_copy = df_copy.reset_index(drop=True)
total_genre_list = []

for idx in range(len(df_copy)):
    for genre in df_copy['genre_list'][idx]:
        total_genre_list.append(genre)

genre_counter =Counter(total_genre_list)
# create list of keys, and a list of values
genre_counter_indx = np.asarray(list(genre_counter.keys()))
genre_counter_val = np.asarray(list(genre_counter.values()))

# create barchart based on genre totals
fig,ax = plt.subplots(figsize=(8,6))
sns.barplot(x = genre_counter_indx, y = genre_counter_val,color='#90caf9',ax=ax)
plt.title('Total Genre')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)
del fig,ax,ticks

#----------STOP AND PRESS SHIFT + ENTER----------
