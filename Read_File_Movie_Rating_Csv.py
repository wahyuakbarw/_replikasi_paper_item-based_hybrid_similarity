import csv
def readFileToList(namaFile):
    # Membuka file 
    with open(namaFile, 'r') as readFile:
        reader = csv.reader(readFile)
        listMovie = list(reader)
    readFile.close()

    listMovieBaru = []
    # Konversi dari string ke integer pada setiap nilai
    for row in listMovie:
        listMovieBaru.append(list(map(int, row)))
    return listMovieBaru


# print(readFileToList('dataTraining1.csv'))

