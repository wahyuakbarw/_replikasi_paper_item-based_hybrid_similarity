# from Create_Data_Rating import createDataRating
# from Import_Data_Training import list_ratings_training
print("Item_Rating_Similarity_Method.py")

def Cosine(matrik, item_t, item_c):
    #Deklarasi variabel
    item_t-=1
    item_c-=1
    pembilang=0
    penyebut=0
    penyebut_t=0
    penyebut_c=0
    #Proses Perhitungan
    for index in range(len(matrik)):
        if (matrik[index][item_t] != 0 and matrik[index][item_c] != 0):
            pembilang += (matrik[index][item_t] * matrik[index][item_c])
            penyebut_t += (matrik[index][item_t] ** 2)
            penyebut_c += (matrik[index][item_c] ** 2)
            
    penyebut = ((penyebut_t)**0.5) * ((penyebut_c)**0.5)
    if (penyebut == 0):
        penyebut = 1
    return pembilang/penyebut

hasil = []
def matriksim(matrik,y):
    for u in range(len(matrik[0])):
        y.append([])
        for i in range(len(matrik[0])):
            if (i == u):
                y[u].append(1.0)
            else:
                y[u].append(Cosine(matrik, i+1, u+1))
    return y

# dataRating = [[3,2,5,4],
# [0,5,1,0],
# [2,5,0,3],
# [2,1,3,2],
# [2,0,5,5]]
# dataRating = createDataRating(list_ratings_training)

import csv
import time
start = time.time()
from Read_File_Movie_Rating_Csv import readFileToList
dataRating = readFileToList("dataTraining1.csv")
hasilItemBased = matriksim(dataRating,hasil)

with open('hasilItemRatingSimilarity1.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(hasilItemBased)

csvFile.close()
end = time.time()
print(end - start)

# for i in hasilItemBased:
#     print(i)