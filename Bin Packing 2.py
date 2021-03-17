
from decimal import *
import time

startTime = time.time()
taxRate = 23.83/21.99

dollarLimit = 29.71/taxRate

sentinel = 0

numGlyphs = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def numToArbBase(num,base):
    
    if num == 0:
        return '0'.zfill(base)
        
    newNumString = ''
    
    while num != 0:
        remainder = num%base
        newNumString = numGlyphs[remainder] + newNumString 
        num = int(num/base)
        
    return newNumString.zfill(base)

prices = [
(4.52	,'Finish Pods        '),
(5.59	,'Bergeon Rodico 6033'),
(5.7	,'Amazon cable       '),
(5.97	,'Finish booster     '),
(5.99	,'Ink                '),
(7.99	,'Solder             '),
(9.74	,'Solder Wick        '),
(9.99	,'Wii HDMI           '),
(9.99	,'Radius Gauges      ')
]

numItems = len(prices)

print(pow(numItems, numItems))

minNumTuples = numItems+1

while sentinel < pow(numItems, numItems):
    #print(sentinel)
    if (sentinel%200000 == 0 or sentinel == pow(numItems, numItems)):
        print(str(sentinel) + '/' + str(pow(numItems, numItems)))
                              
    distro = (numToArbBase(sentinel, numItems))
               #^ Gets the current bin distribution in string form.
    
    distroList = list(distro)
    #^ Gets the current bin distribution in list form.
        
    distinctBins = list(set(distroList))
    #^ Gets the list of distinct bins.
    
    distinctBins.sort()    
               #^ Sorts the distinct bins.
    
    numBins = len(distinctBins)
    #^ Figures out how many distinct bin there are.
    
    currentListOfTuples = []
    
    for distinctItem in distinctBins:
        binTuple = []
        for itemNum, binNum in enumerate(distroList):
            if (binNum == distinctItem):
                binTuple.append(itemNum)
        
        currentListOfTuples.append(tuple(binTuple))
        
        #num  012
        #buck 101
        #dist 01
        
        #item 0 goes in bucket 2
        #item 1 goes in bucket 1
        #item 2 goes in bucket 2, etc...

    allBinSums = []
    for singleTuple in currentListOfTuples:
        binSum = 0
        for singleElement in singleTuple:
            binSum += prices[singleElement][0]        
        binSum = round(binSum, 2)
        allBinSums.append(binSum)

    sentinel += 1
               
    if any(ele > dollarLimit for ele in allBinSums):
                continue
    else:
        if len(currentListOfTuples) < minNumTuples:
            minNumTuples = len(currentListOfTuples)
            bestTuple = currentListOfTuples

for tupleObj in bestTuple:
    tupleSum = 0
    for el in tupleObj:
        tupleSum += prices[el][0]
        tupleSum = round(tupleSum, 2)
    print(tupleSum)

print(bestTuple)

endTime = time.time()
print(f"Runtime of the program is {endTime - startTime}")
