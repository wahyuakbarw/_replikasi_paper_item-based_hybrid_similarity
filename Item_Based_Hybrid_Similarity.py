hasilCosine = [[1.0, 0.7970533969860858, 0.9788389158235425, 0.9502621934663978],
[0.7970533969860858, 1.0, 0.5554920598635308, 0.847579379526013],
[0.9788389158235425, 0.5554920598635308, 0.9999999999999999, 0.9897782665572894],
[0.9502621934663978, 0.847579379526013, 0.9897782665572894, 1.0]]

hasilItem = [[1.0, 0.0, 0.8, 0.4],
            [0.0, 1.0, 0.2, 0.6],
            [0.8, 0.2, 1.0, 0.6],
            [0.4, 0.6, 0.6, 1.0]]

tabelRating = [[3,2,5,4],
[0,5,1,0],
[2,5,0,3],
[2,1,3,2],
[2,0,5,5]]

#Menduplikasi tabel rating
tabelRating_template = tabelRating

def mean(tabelRating, item):
    item-=1
    jumlah=0
    banyak=0
    for i in range(len(tabelRating)):
        if (tabelRating[i][item]!=0):
            jumlah+= tabelRating[i][item]
            banyak+=1
    return jumlah/banyak

def hybrid(hasilCosine, hasilItem, user, item):
    rataRataItem = mean(tabelRating, item)
    pembilang, penyebut = 0,0
    for k in range(1, len(hasilCosine)+1):
        #Tetangga dan User sudah memprediksi item tetangga
        if (k-1 != item-1 and tabelRating[user-1][k-1] != 0):

            pembilang += (hasilCosine[item-1][k-1] * hasilItem[item-1][k-1] *
                (tabelRating[user-1][k-1] - mean(tabelRating, k)))

            penyebut += abs(hasilCosine[item-1][k-1] * hasilItem[item-1][k-1])

    return (rataRataItem + (pembilang/penyebut))

for row in range(len(tabelRating)):
    for column in range(len(tabelRating[row])):
        if (tabelRating[row][column] == 0):
            print("Prediksi Rating pada User %i Item %i adalah %s"% (row+1, column+1, 
            hybrid(hasilCosine, hasilItem, row+1, column+1)) )
            tabelRating_template[row][column] = hybrid(hasilCosine, hasilItem, row+1, column+1)
print (tabelRating_template)