
'''[user_id, movie_id, rating]'''

originalDatasets = [[1, 1, 3],
            [1, 2, 2],
            [1, 3, 5],
            [1, 4, 4],
            [2, 1, 0],
            [2, 2, 5],
            [2, 3, 1],
            [2, 4, 0],
            [3, 1, 2],
            [3, 2, 5],
            [3, 3, 0],
            [3, 4, 3],
            [4, 1, 2],
            [4, 2, 1],
            [4, 3, 3],
            [4, 4, 2],
            [5, 1, 2],
            [5, 2, 0],
            [5, 3, 5],
            [5, 4, 5]]

jumlah_movie = 4
movie_id = 0
temp = []
hasil = []

for i in range(len(originalDatasets)):

    temp.append(originalDatasets[i][2])
    movie_id += 1
    if movie_id == jumlah_movie:
        movie_id = 0
        hasil.append(temp)
        temp = []
    
for i in hasil:
    print(i, end='\n')













