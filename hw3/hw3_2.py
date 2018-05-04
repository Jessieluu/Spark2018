import random
card = []
minhash = []
hashValue = Matrix

i = 1
while i < = hashValue:
    card.append(i)
    i += 1

temp = len(card)-1
while temp != 0:
    temp = random.randrange(temp)
    minhash.append( card[temp] )
    card[temp] = card[temp]
    temp -= 1

minhash.append(card[0])
hashAll = shingleAns.collect()
hashAns = hashAll[minhash.index(1)]
findValue = 2

while (findValue <= len(minhash)) & (0 in hashAns):
    findList = hashAll[minhash.index(findValue)]
    while (1 in findList):
        if hashAns[findList.index(1)] == 0:
            hashAns[findList.index(1)] = findValue
        findList[findList.index(1)] = 0
    findValue += 1
    
filename = "hw3_2.txt"
with open( filename, 'w', newline='') as out:
    out.write ( str(hashAns) )
print ("Finished!")