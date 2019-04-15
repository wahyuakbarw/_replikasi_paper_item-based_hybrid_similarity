import copy

hasilItemBased = [[1.0, 0.7970533969860858, 0.9788389158235425, 0.9502621934663978],
[0.7970533969860858, 1.0, 0.5554920598635308, 0.847579379526013],
[0.9788389158235425, 0.5554920598635308, 1.0, 0.9897782665572894],
[0.9502621934663978, 0.847579379526013, 0.9897782665572894, 1.0]]


hasilItemAttribute = [[1.0, 0.0, 0.8, 0.4],
            [0.0, 1.0, 0.2, 0.6],
            [0.8, 0.2, 1.0, 0.6],
            [0.4, 0.6, 0.6, 1.0]]

item = 1
jumlahTetangga = 2
hasilItemBasedPerItem = copy.deepcopy(hasilItemBased[item-1])
hasilItemBasedPerItem.sort(reverse=True)
listTetangga = []
for i in range(jumlahTetangga):
    listTetangga+=[hasilItemBasedPerItem[i+1]]
# print(hasilItemBasedPerItem)
print(listTetangga)
listIndexTetangga = []
for i in listTetangga:
    listIndexTetangga.append(hasilItemBased[item-1].index(i)+1)
print(listIndexTetangga)
