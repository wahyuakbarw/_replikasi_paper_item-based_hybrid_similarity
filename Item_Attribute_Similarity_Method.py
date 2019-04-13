dataAttribute = [[1, 0, 1, 1, 0],
                 [0, 1, 0, 0, 1],
                 [1, 0, 1, 1, 1],
                 [0, 1, 1, 1, 1]]


temp = dataAttribute
hasil_similarity_item_attribute = []

def calculate(a, b):
    hasil = 0
    i = 0
    while i < len(a):
        if a[i] == b[i]:
            hasil+=1
        i+=1
    return hasil/len(a)
    

for a in range(len(dataAttribute)):
    k = []
    for b in range(len(temp)):
        k.append(calculate(dataAttribute[a], temp[b]))
    hasil_similarity_item_attribute.append(k)

for i in hasil_similarity_item_attribute:
    print(i)
