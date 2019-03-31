import pandas as pd
import numpy as np

genres = ['Unknown','Action','Adventure','Animation','Children\'s','Comedy','Crime','Documentary','Drama',
'Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']

#create a Series with an arbitrary list
# s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
# print(type(s))
# print(s)

# pass in column names for each CSV
users_cols = ['user_id','age','sex','occupation','zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=users_cols,encoding='latin-1')

ratings_cols = ['user_id','movie_id','rating','unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data',sep='\t',names=ratings_cols, encoding='latin-1')

#the movies file contains columns indicating the movie's genres
#let's only load the first five columns of the file with usecols
movie_cols = ['movie_id','title','release_date','video_release_date','imdb_url', 
genres[0],genres[1],genres[2],genres[3],genres[4],genres[5],genres[6],genres[7],genres[8],
genres[9],genres[10],genres[11],genres[12],genres[13],genres[14],genres[15],genres[16],genres[17],genres[18]]
movies = pd.read_csv('ml-100k/u.item',sep='|',names=movie_cols,encoding='latin-1')

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)

most_rated = lens.groupby('title').size().sort_values(ascending=False)[:25]

movie_stats = lens.groupby('title').agg({'rating':[np.size, np.mean]})

#Konversi DataFrame ke List.
listMovies = movies.values.tolist()

#Membuat list data atribut movie.
newListMovies = [[] for _ in range(len(listMovies))]
print(newListMovies)
for indexMovie in range(len(listMovies)):
    for indexInMovie in range(len(listMovies[indexMovie])):
        if (indexInMovie==1 or indexInMovie==5 or indexInMovie==6 or indexInMovie==7 or indexInMovie==8 or indexInMovie==9 or indexInMovie==10 or indexInMovie==11 or indexInMovie==12 or indexInMovie==13 or indexInMovie==14 or indexInMovie==15 or indexInMovie==16 or indexInMovie==17 or indexInMovie==18):
            newListMovies[indexMovie].append(listMovies[indexMovie][indexInMovie])

print(newListMovies)