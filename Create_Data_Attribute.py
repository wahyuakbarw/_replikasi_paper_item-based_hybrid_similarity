import pandas as pd

genres = ['Unknown','Action','Adventure','Animation','Children\'s','Comedy','Crime','Documentary','Drama',
'Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']

#the movies file contains columns indicating the movie's genres
#let's only load the first five columns of the file with usecols
movie_cols = ['movie_id','title','release_date','video_release_date','imdb_url', 
genres[0],genres[1],genres[2],genres[3],genres[4],genres[5],genres[6],genres[7],genres[8],
genres[9],genres[10],genres[11],genres[12],genres[13],genres[14],genres[15],genres[16],genres[17],genres[18]]
movies = pd.read_csv('ml-100k/u.item',sep='|',names=movie_cols,encoding='latin-1')

#Konversi DataFrame ke List.
listMovies = movies.values.tolist()

#Membuat list kosong [[],[]....[]]
newListMovies = [[] for _ in range(len(listMovies))]

# list berisi index 5 sampai 18
listIndexMovie = [i for i in range(5,19)]

#Membuat list data atribut movie.
for indexMovie in range(len(listMovies)):
    for indexInMovie in range(len(listMovies[indexMovie])):
        if (indexInMovie in listIndexMovie):
            newListMovies[indexMovie].append(listMovies[indexMovie][indexInMovie])
# print(newListMovies)

"""
    Hasilnya [[nama film, genres[0], genres[1],genres[2],genres[3],genres[4],genres[5],genres[6],genres[7],
    genres[8], genres[9],genres[10],genres[11],genres[12],genres[13],genres[15],genres[16],genres[17],
    genres[18], ['Blablabla', 0, 1,0,1, .... 1]]
"""