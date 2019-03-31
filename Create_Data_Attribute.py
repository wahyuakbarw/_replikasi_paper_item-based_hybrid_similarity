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
print(newListMovies)

#Membuat list data atribut movie.
for indexMovie in range(len(listMovies)):
    for indexInMovie in range(len(listMovies[indexMovie])):
        if (indexInMovie==1 or indexInMovie==5 or indexInMovie==6 or indexInMovie==7 or indexInMovie==8 or indexInMovie==9 or indexInMovie==10 or indexInMovie==11 or indexInMovie==12 or indexInMovie==13 or indexInMovie==14 or indexInMovie==15 or indexInMovie==16 or indexInMovie==17 or indexInMovie==18):
            newListMovies[indexMovie].append(listMovies[indexMovie][indexInMovie])
print(newListMovies)

"""
    Hasilnya [[nama film, genres[0], genres[1],genres[2],genres[3],genres[4],genres[5],genres[6],genres[7],
    genres[8], genres[9],genres[10],genres[11],genres[12],genres[13],genres[15],genres[16],genres[17],
    genres[18], ['Blablabla', 0, 1,0,1, .... 1]]
"""