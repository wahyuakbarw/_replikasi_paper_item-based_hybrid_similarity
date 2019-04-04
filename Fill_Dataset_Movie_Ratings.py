""" DiPanggil 1 Kali  """

import csv
from Create_Data_Rating import listMovieRatings

def sortDuaIndex(sebuahList):
    return sebuahList[0:2]

listMovieRatingsComplete = [[] for _ in range(1682*943)]

jumlah_user = 943
jumlah_movie = 1682

list_tambahan = []
temp_list = []

for i in listMovieRatings:
    list_tambahan.append(i[:2])
    print(i)

for i in range(1, jumlah_user + 1):
    for j in range(1, jumlah_movie + 1):
        if [i, j] not in list_tambahan:
            temp_list.append([i, j, 0])
            print([i, j])

# for x in temp_list:
#     print(x, end='\n')
listMovieRatingsComplete = listMovieRatings + temp_list
listMovieRatingsComplete.sort(key=sortDuaIndex)
print(len(listMovieRatingsComplete))

#Menyimpan Movie Rating di csv
with open('movie_rating.csv', "w") as writeFile:
   writer = csv.writer(writeFile)
   writer.writerows(listMovieRatingsComplete)
writeFile.close()
