import csv
with open('movie_rating.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    listMovie = list(reader)
readFile.close()

#Menghilangkan list kosong
#digunakan ketika ada list yang kosong diantara data
listMovieBaru = []
for i in listMovie:
    if (len(i) != 0):
        listMovieBaru.append(i)
print(listMovieBaru)

#mengonversi ke integer
#digunakan ketika data menjadi string semua
for i in range(len(listMovieBaru)):
    for j in range(len(listMovieBaru[i])):
        listMovieBaru[i][j] = int(listMovieBaru[i][j])
print(listMovieBaru)
