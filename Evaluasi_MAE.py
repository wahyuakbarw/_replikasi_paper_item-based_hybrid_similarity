# import pandas

# # Mengambil data training fold 1
# ratings_cols = ['user_id','movie_id','rating','unix_timestamp']
# ratings_training = pandas.read_csv('ml-100k/u1.base',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_training.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)
# # Mengambil data test fold 2
# ratings_cols = ['user_id','movie_id','rating','unix_timestamp']
# ratings_test = pandas.read_csv('ml-100k/u1.test',sep='\t',names=ratings_cols,usecols=range(3), encoding='latin-1')
# ratings_test.sort_values(['user_id','movie_id'], axis=0, ascending=True, inplace=True)

# print("Training \n", ratings_training)
# print("Test \n", ratings_test)

from Item_Based_Hybrid_Similarity import hybrid

dataTraining = [[3,2,5,4],
[0,5,1,0],
[2,5,0,3],
[2,1,3,2],
[2,0,5,5]]

dataTraining_menjadiDataLengkap = dataTraining

dataTest = [[0,0,0,0],
[2,0,0,4],
[0,0,3,0],
[0,0,0,0],
[0,3,0,0]]

hasilItem = [[1.0, 0.0, 0.8, 0.4],
            [0.0, 1.0, 0.2, 0.6],
            [0.8, 0.2, 1.0, 0.6],
            [0.4, 0.6, 0.6, 1.0]]

hasilCosine = [[1.0, 0.7970533969860858, 0.9788389158235425, 0.9502621934663978],
[0.7970533969860858, 1.0, 0.5554920598635308, 0.847579379526013],
[0.9788389158235425, 0.5554920598635308, 0.9999999999999999, 0.9897782665572894],
[0.9502621934663978, 0.847579379526013, 0.9897782665572894, 1.0]]


for row in range(len(dataTraining)):
    for column in range(len(dataTraining[row])):
        if (dataTraining[row][column] == 0 and dataTest[row][column] != 0):
            dataTraining_menjadiDataLengkap[row][column] = hybrid(hasilCosine, hasilItem, row+1, column+1)

# Menghitung MAE
penyebut = 0
pembilang = 0
for row in range(len(dataTraining)):
    for column in range(len(dataTraining[row])):
        if (dataTest[row][column] != 0):
            pembilang += abs(dataTraining_menjadiDataLengkap[row][column] - 
            dataTest[row][column])
            penyebut += 1
MAE = pembilang/penyebut
print(MAE)