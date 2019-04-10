listData = [[1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [0, 1, 1, 1, 1]]

temp_x = listData
hasilx = []

def calculate(a, b):
    hasil = 0
    i = 0
    while i < len(a):
        if a[i] == b[i]:
            hasil+=1
        i+=1
    return hasil/len(a)
    

for a in range(len(listData)):
    k = []
    for b in range(len(temp_x)):
        k.append(calculate(listData[a], temp_x[b]))
    hasilx.append(k)

for i in hasilx:
    print(i)
