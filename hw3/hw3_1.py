
# coding: utf-8

# In[2]:

from bs4 import BeautifulSoup
import os.path
import os
import time
import re
import codecs
import string
import binascii

documents = []
selectedbody = {}

print("Reading files....")

t0 = time.time()

data = ''

for file in os.listdir("data/"):
    if file.endswith(".sgm"):
        filename = os.path.join("data", file)
        f = codecs.open(filename, 'r', encoding='utf-8', errors='ignore')
        data = data + f.read()
        
print("It took %.2f sec to read data" % (time.time() - t0))

print("Preparing for data...")

t1 = time.time()
soup = BeautifulSoup(data, "html.parser")
bodies = soup.findAll('body')

i = 0
for body in bodies:
    selectedbody[i] = body
    documents.append( re.sub(' +', ' ', str(body)                     .replace("<body>", "").replace("</body>", "")                     .translate(str.maketrans('', '', string.punctuation))                     .replace("", "").replace("\n", " ").lower() ) )
    i += 1

print("It took %.2f sec to prepare data" % (time.time() - t0))

print("The number of documents size is:" + str(len(documents)))

i = 0
d = {}
t = {}
t2 = time.time()

for value in documents:
    d[i] = value  #create a dictionary where value = document text and key = docid
    d[i] = re.sub("[^\w]", " ", d[i]).split() #split text into word
    
    if d[i]:  #remove rows with empty values from dictionary d
        i += 1
    else:
        del d[i]
        del body[i]


# In[ ]:

# =============================================
#       Calculate k-shingles
# =============================================

shinglesets = {}
docNames = []

totalshingles = 0
shingleNo = 0

###get input k for shingle
while True:
    try:
        shingle_size = int(input("Please enter k value for k-shingles:"))
    except ValueError:
        print("Your input is not valid.")
        continue
    if shingle_size <=0:
        continue
    else:
        break
        
print("Shingling articles..")

shinglesInAll = set()

t3 = time.time()
for i in range(0, len(d)):
    words = d[i]
    
    docID = i
    
    docNames.append(docID)
    
    shinglesInDocWords = set()
    shinglesInDocInts = set()
    
    shingle = []
    
    for index in range(len(words) - shingle_size +1):
        shingle = words[index:index + shingle_size]
        shingle = ' '.join(shingle)
        
        crc = binascii.crc32(str.encode(shingle)) & 0xffffffff

        if shingle not in shinglesInAll:
            shinglesInAll.add(shingle)
        
        if shingle not in shinglesInDocWords:
            shinglesInDocWords.add(shingle)
            
        if crc not in shinglesInDocInts:
            shinglesInDocInts.add(crc)
            shingleNo = shingleNo + 1
        else:
            del shingle
            index = index -1
        
    shinglesets[docID] = shinglesInDocInts

totalshingles = shingleNo

print("Total Number of Shingles", shingleNo)
print("\nShingling " + str(len(shinglesets)) + " docs took %.2f sec." % (time.time() - t3))
print("\nAverage shingles per doc: %.2f" % (shingleNo / len(shinglesets)))

import numpy as np

# doc_set = set(documents[0])
Matrix = []

t4 = time.time()
for i in shinglesInAll:
    tmp = []
    # print(i)
    for j in range(0, 5):
        if i in documents[j]:
            boolean = 1
            tmp.append(boolean)
        else:
            boolean = 0
            tmp.append(boolean)
    Matrix.append(tmp)
print("\nMaking matrix took %.2f sec." % (time.time() - t4))

print("Start output in " + str(shingle_size) + " - shingles")              
with open("hw3_1_" + str(shingle_size) + " - shingles.txt", 'a') as file:
    for i in range(0, len(shinglesInAll)):
        for j in range(0, 5):
            file.write(str(Matrix[i][j]))
        file.write("\n")
        
print("finish!")


# In[ ]:



