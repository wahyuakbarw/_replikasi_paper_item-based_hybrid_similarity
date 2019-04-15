import pandas
print("Import_Data_Training.py")

ratings_cols = ['user_id','movie_id','rating','unix_timestamp']

# # Menyimpan Data Training 1 ke DataFrame
# ratings_training_1 = pandas.read_csv('ml-100k/u1.base',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_training_1.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_training = ratings_training_1.values.tolist()

# # Menyimpan Data Test 1 ke DataFrame
# ratings_test_1 = pandas.read_csv('ml-100k/u1.test',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_test_1.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_test = ratings_test_1.values.tolist()

# # Menyimpan Data Training 2 ke DataFrame
# ratings_training_2 = pandas.read_csv('ml-100k/u2.base',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_training_2.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_training = ratings_training_2.values.tolist()

# # Menyimpan Data Test 2 ke DataFrame
# ratings_test_2 = pandas.read_csv('ml-100k/u2.test',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_test_2.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_test = ratings_test_2.values.tolist()

# # Menyimpan Data Training 3 ke DataFrame
# ratings_training_3 = pandas.read_csv('ml-100k/u3.base',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_training_3.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_training = ratings_training_3.values.tolist()

# # Menyimpan Data Test 3 ke DataFrame
# ratings_test_3 = pandas.read_csv('ml-100k/u3.test',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_test_3.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_test = ratings_test_3.values.tolist()

# # Menyimpan Data Training 4 ke DataFrame
# ratings_training_4 = pandas.read_csv('ml-100k/u4.base',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_training_4.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_training = ratings_training_4.values.tolist()

# # Menyimpan Data Test 4 ke DataFrame
# ratings_test_4 = pandas.read_csv('ml-100k/u1.test',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_test_4.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_test = ratings_test_4.values.tolist()

# # Menyimpan Data Training 5 ke DataFrame
# ratings_training_5 = pandas.read_csv('ml-100k/u5.base',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_training_5.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_training = ratings_training_5.values.tolist()

# # Menyimpan Data Test 5 ke DataFrame
# ratings_test_5 = pandas.read_csv('ml-100k/u5.test',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_test_5.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Convert DataFrame to List
# list_ratings_test = ratings_test_5.values.tolist()
