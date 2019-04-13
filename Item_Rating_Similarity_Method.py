
def Cosine(matrik, item_t, item_c):
    #Deklarasi variabel
    item_t-=1;item_c-=1; pembilang=0; penyebut=0; penyebut_t=0;penyebut_c=0;

    #Proses Perhitungan
    for index in range(len(matrik)):
        if (matrik[index][item_t] != 0 and matrik[index][item_c] != 0):
            pembilang += (matrik[index][item_t] * matrik[index][item_c])
            penyebut_t += (matrik[index][item_t] ** 2)
            penyebut_c += (matrik[index][item_c] ** 2)
            
    penyebut = ((penyebut_t)**0.5) * ((penyebut_c)**0.5)
    return pembilang/penyebut

hasil = []
def matriksim(matrik,y):
    for u in range(len(matrik[0])):
        y.append([])
        for i in range(len(matrik[0])):
            y[u].append(Cosine(matrik, i+1, u+1))
    return y

dataRating = [[3,2,5,4],
[0,5,1,0],
[2,5,0,3],
[2,1,3,2],
[2,0,5,5]]

hasilItemBased = matriksim(dataRating,hasil)

for i in hasilItemBased:
    print(i)