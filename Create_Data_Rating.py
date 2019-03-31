import pandas as pd

# pass in column names for each CSV
ratings_cols = ['user_id','movie_id','rating','unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
ratings.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
print(ratings)

#konversi DataFrame ke List
listMovieRatings = ratings.values.tolist()

"""
Hasilnya adalah [[User ID, Movie ID, Rating], [1, 1, 5]....[943, 1330, 3]]
"""

