import pandas

# pass in column names for each CSV
# ratings_cols = ['user_id','movie_id','rating','unix_timestamp']
# ratings = pandas.read_csv('ml-100k/u.data',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# print(ratings)

ratings_cols = ['user_id','movie_id','rating','unix_timestamp']

# Menyimpan Data Training 1 ke DataFrame
ratings_training_1 = pandas.read_csv('ml-100k/u1.base',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
ratings_training_1.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# Convert DataFrame to List
list_ratings_training = ratings_training_1.values.tolist()

# Menyimpan Data Test 1 ke DataFrame
ratings_test_1 = pandas.read_csv('ml-100k/u1.test',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
ratings_test_1.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# Convert DataFrame to List
list_ratings_test = ratings_test_1.values.tolist()


"""
Hasilnya adalah [[User ID, Movie ID, Rating], [1, 1, 5]....[943, 1330, 3]]
"""

