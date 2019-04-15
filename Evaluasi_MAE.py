import time
start = time.time()
# from Import_Data_Training import list_ratings_test
# from Create_Data_Rating import createDataRating
# from Item_Rating_Similarity_Method import hasilItemBased, dataRating
from Item_Attribute_Similarity_Method import hasilItemAttribute
from Read_File_Movie_Rating_Csv import readFileToList
from Item_Based_Hybrid_Similarity_V2 import hybrid
import matplotlib.pyplot as plt
import numpy as np

# Data Training
dataTraining = readFileToList("dataTraining1.csv")
# Data Test
dataTest = readFileToList("dataTest1.csv")
# Hasil Item Based Similarity
hasilItemBased = readFileToList("hasilItemRatingSimilarity1.csv")
# Hasil Item Attribute Similarity
hasilItemAttribute = hasilItemAttribute

def MeanAbsoluteError(numberOfNeighbour):

    # Menghitung MAE
    penyebut = 0
    pembilang = 0
    for row in range(len(dataTraining)):
        for column in range(len(dataTraining[row])):
            if (dataTest[row][column] != 0):
                # Prediksi rating dikurangi rating sesungguhnya
                pembilang += abs(hybrid(dataTraining, hasilItemBased, hasilItemAttribute, row+1, column+1, numberOfNeighbour) - dataTest[row][column])
                # Banyaknya rating sesungguhnya
                penyebut += 1

    # Hasil MAE
    MAE = pembilang/penyebut
    print("Hasil MAE =",MAE)
    return MAE

jumlahTetangga = [2, 5, 10, 15, 20, 25, 30, 35, 40]
hasilMAE = []
for tetangga in jumlahTetangga:
    hasilMAE.append(MeanAbsoluteError(tetangga))

y_pos = np.arange(len(jumlahTetangga))
plt.bar(y_pos, hasilMAE, align='center', color='green')
plt.xticks(y_pos, jumlahTetangga)
plt.ylim([0.73, 0.89])
plt.yticks(np.arange(0.73, 0.89, 0.02))
plt.xlabel('Number of Neighbours')
plt.ylabel('MAE')
plt.title('The Result of MAE by adjusting the value of k-neighbors')
plt.show()
end = time.time()
print("Waktu =", str(start-end))

# print(jumlahTetangga)
# print(hasilMAE)

# dataTraining = [[3,2,5,4],
# [0,5,1,0],
# [2,5,0,3],
# [2,1,3,2],
# [2,0,5,5]]

# dataTest = [[0,0,0,0],
# [1,0,0,3],
# [0,0,4,0],
# [0,0,0,0],
# [0,5,0,0]]

# hasilItemAttribute = [[1.0, 0.0, 0.8, 0.4],
#             [0.0, 1.0, 0.2, 0.6],
#             [0.8, 0.2, 1.0, 0.6],
#             [0.4, 0.6, 0.6, 1.0]]

# hasilItemBased = [[1.0, 0.7970533969860858, 0.9788389158235425, 0.9502621934663978],
# [0.7970533969860858, 1.0, 0.5554920598635308, 0.847579379526013],
# [0.9788389158235425, 0.5554920598635308, 1.0, 0.9897782665572894],
# [0.9502621934663978, 0.847579379526013, 0.9897782665572894, 1.0]]
