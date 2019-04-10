# -*- coding: utf-8 -*-
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
    #print(matrik)
    u-=1;v-=1; pembilang=0; penyebut=0; p1=0;p2=0;
    for i in range(len(matrik)):
        if (matrik[i][u] != 0 and matrik[i][v] != 0):
     #       print(i)
            pembilang += (meanCenteredRating(matrik, i, u) * meanCenteredRating(matrik, i, v))
            p1 += (meanCenteredRating(matrik, i, u) ** 2)
            p2 += (meanCenteredRating(matrik, i, v) ** 2)
            
    penyebut = math.sqrt(p1) * math.sqrt(p2)
    #print ("Penyebut",penyebut)
    #print(penyebut);print(pembilang);print(p1);print(p2);
    return pembilang/float(penyebut)

y = []
def matriksim(matrik,y):
    for u in range(len(matrik[0])):
        y.append([])
        for i in range(len(matrik[0])):
            y[u].append(adjustedCosine(matrik, i+1, u+1))
    print(y)

matrik = [[3,2,5,4],
[0,5,1,0],
[2,5,0,3],
[2,1,3,2],
[2,0,5,5]]

    
matriksim(matrik,y)
