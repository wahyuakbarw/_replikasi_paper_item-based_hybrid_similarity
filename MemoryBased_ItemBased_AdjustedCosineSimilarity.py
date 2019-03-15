import math

def miu(matrik, u):
    pembilang = 0
    penyebut = 0
    for i in matrik[u]:
        if i != 0:
            pembilang+=i
            penyebut+=1
    return (pembilang/penyebut)

def meanCenteredRating(matrik, u, j):
    return matrik[u][j] - miu(matrik, u)

def adjustedCosine(matrik, u, v):
    print(matrik)
    u-=1;v-=1; pembilang=0; penyebut=0; p1=0;p2=0;
    for i in range(len(matrik)):
        if (matrik[i][u] != 0 and matrik[i][v] != 0):
            # print(i)
            pembilang += (meanCenteredRating(matrik, i, u) * meanCenteredRating(matrik, i, v))
            p1 += (meanCenteredRating(matrik, i, u) ** 2)
            p2 += (meanCenteredRating(matrik, i, v) ** 2)
    penyebut = math.sqrt(p1) + math.sqrt(p2)
    # print(penyebut);print(pembilang);print(p1);print(p2);
    return pembilang/float(penyebut)

matrik = [[7,6,7,4,5,4],
[6,7,0,4,3,4],
[0,3,3,1,1,0],
[1,2,2,3,3,4],
[1,0,1,2,3,3]]

print(adjustedCosine(matrik, 1, 1))