import csv
import copy



print("Create_Data_Rating.py")

def createDataRating(listRatings):
    listMovieRatingsComplete = []
    jumlah_user = 943
    jumlah_movie = 1682

    ratingTiapUser = []
    banyakDataUser = 0
    banyakDataUserSementara = copy.deepcopy(banyakDataUser)
    cek = True
    
    for row in range(1, jumlah_user+1):
        for column in range(1, jumlah_movie+1):
            # Perulangan untuk melihat Dataset Asli
            for indexForCheck in range(banyakDataUserSementara, len(listRatings)):
                if listRatings[indexForCheck][0] == row:
                    if listRatings[indexForCheck][1] == column:
                        cek = False
                        banyakDataUser+=1
                        break
                    else:
                        cek = True
                else:
                    break
            # Jika User tidak merating Item maka ratingnya bernilai 0
            if cek == True:
                ratingTiapUser += [0]
            else:
                ratingTiapUser += [listRatings[indexForCheck][2]]
        # Untuk melanjutkan pencarian pada data asli tanpa perlu mengulangi dari index awal
        banyakDataUserSementara += banyakDataUser
        banyakDataUser = 0
        # Menambah data rating seorang user ke list semua rating
        listMovieRatingsComplete += [ratingTiapUser]
        ratingTiapUser = []

    # print(listMovieRatingsComplete[0])
    return listMovieRatingsComplete

# import csv
# from Import_Data_Training import  list_ratings_test, list_ratings_training

# with open('dataTraining1.csv', 'w', newline='') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(createDataRating(list_ratings_training))

# csvFile.close()

# with open('dataTest1.csv', 'w', newline='') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(createDataRating(list_ratings_test))

# csvFile.close()