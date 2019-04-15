# from Create_Data_Rating import createDataRating
# from Import_Data_Training import list_ratings_training
# from Item_Attribute_Similarity_Method import hasilItemAttribute
# from Item_Rating_Similarity_Method import hasilItemBased


# Fungsi menentukan rata-rata suatu item
def mean(tabelRating, item):
    item-=1
    jumlah=0
    banyak=0
    for i in range(len(tabelRating)):
        # Kondisi jika user tidak memberikan item
        if (tabelRating[i][item]!=0):
            jumlah += tabelRating[i][item]
            banyak += 1
    return jumlah/banyak

# Fungsi menentukan prediksi rating
def hybrid(tabelRating, hasilItemBased, hasilItemAttribute, user, item, numberOfNeighbour):
    rataRataItem = mean(tabelRating, item)
    pembilang, penyebut = 0,0
    for k in range(1, len(hasilItemBased)+1):
        #Tetangga dan User sudah memprediksi item tetangga
        if (k-1 != item-1 and tabelRating[user-1][k-1] != 0):

            pembilang += (hasilItemBased[item-1][k-1] * hasilItemAttribute[item-1][k-1] *
                (tabelRating[user-1][k-1] - mean(tabelRating, k)))

            penyebut += abs(hasilItemBased[item-1][k-1] * hasilItemAttribute[item-1][k-1])

    return (rataRataItem + (pembilang/penyebut))





# hasilItemBased = [[1.0, 0.7970533969860858, 0.9788389158235425, 0.9502621934663978],
# [0.7970533969860858, 1.0, 0.5554920598635308, 0.847579379526013],
# [0.9788389158235425, 0.5554920598635308, 1.0, 0.9897782665572894],
# [0.9502621934663978, 0.847579379526013, 0.9897782665572894, 1.0]]


# hasilItemAttribute = [[1.0, 0.0, 0.8, 0.4],
#             [0.0, 1.0, 0.2, 0.6],
#             [0.8, 0.2, 1.0, 0.6],
#             [0.4, 0.6, 0.6, 1.0]]

# tabelRating = [[3,2,5,4],
# [0,5,1,0],
# [2,5,0,3],
# [2,1,3,2],
# [2,0,5,5]]
# tabelRating = createDataRating(list_ratings_training)

#Menduplikasi tabel rating
# tabelRating_template = tabelRating
# for row in range(len(tabelRating)):
#     for column in range(len(tabelRating[row])):
#         if (tabelRating[row][column] == 0):
#             print("Prediksi Rating pada User %i Item %i adalah %s"% (row+1, column+1, 
#             hybrid(tabelRating, hasilItemBased, hasilItemAttribute, row+1, column+1)) )
#             tabelRating_template[row][column] = hybrid(tabelRating, hasilItemBased, hasilItemAttribute, row+1, column+1)
# print (tabelRating_template)