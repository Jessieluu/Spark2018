
# coding: utf-8

# In[ ]:

# =================================
#       Calculate LSH
# =================================

lsh = []
fixOneList = []
i = 0

while(i < len(bodyColumn)):
    ans = shingleAns.map(lambda x : x[i]).zipWithIndex().filter(lambda x: x[0]==1).map(lambda x : x[1]).collect()
    fixOneList.append(ans)
    i+=1

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
        s = len(tempMolecular) / len(tempDenominator)
        tempLSH = 1-(1-s)
        tempList = (i, j, tempLSH)
        lsh.append(tempList)
        j+=1
    i+=1

with open("hw3_3.txt", 'w', newline='') as out:
    out.write(str(lsh))

