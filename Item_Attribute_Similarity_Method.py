from Create_Data_Attribute import newListMovies
print("Item_Attribute_Similarity_Method.py")

# dataAttribute = [[1, 0, 1, 1, 0],
#                  [0, 1, 0, 0, 1],
#                  [1, 0, 1, 1, 1],
#                  [0, 1, 1, 1, 1]]
dataAttribute = newListMovies
temp = dataAttribute

hasil_similarity_item_attribute = []
    
for at in range(len(dataAttribute)):
    k = []
    for ac in range(len(temp)):
        k.append(len([i for i, j in zip(dataAttribute[at], temp[ac]) if i == j])/len(dataAttribute[at]))
    hasil_similarity_item_attribute.append(k)

hasilItemAttribute = hasil_similarity_item_attribute
# print(hasilItemAttribute)

# for i in hasilItemAttribute:
#     print(i)
