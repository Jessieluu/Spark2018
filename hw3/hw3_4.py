
# coding: utf-8

# In[ ]:

# ==================================
#       Calculate KNN
# ==================================

knn = []

i = 0
while(i <= len(bodyColumn)-2):
    j = i+1
    while(j <= len(bodyColumn)-1):
        tempMolecular = []
        tempDenominator = []
        mergeLists = fixOneList[i] + fixOneList[j]
        for mergeList in mergeLists:
            if mergeList not in tempDenominator:
                tempDenominator.append(mergeList)
            else:
                tempMolecular.append(mergeList)
        tempD = (len(fixOneList[i]) * len(fixOneList[j]))
        if tempD == 0:
            s = 0
        else:
            s = len(tempMolecular) / tempD
        tempKNN = (i,j,s)
        knn.append(tempKNN)
        j+=1
    i+=1

tempLSH = sc.parallelize(lsh)
tempKNN = sc.parallelize(knn)
avgLSH = tempLSH.map(lambda x : x[2]).sum()/tempLSH.count()
avgKNN = tempKNN.map(lambda x : x[2]).sum()/tempKNN.count()

with open( "hw3_4.txt", 'w', newline='') as out:
    out.write ("avgLSH" + str(avgLSH))
    out.write ("avgKNN" + str(avgKNN))

