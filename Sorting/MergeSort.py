import random,sys

def merge(array,leftIndex,rightIndex,middle):
    leftCopyIndex = middle  - leftIndex +   1
    rightCopyIndex = rightIndex - middle 
    mainIndex = leftIndex
    
    leftCopy = [0] * (leftCopyIndex) 
    rightCopy = [0] * (rightCopyIndex) 
    for i in range(0,leftCopyIndex):
        leftCopy[i] = array[i+leftIndex]
    
    for j in range(0,rightCopyIndex):
        rightCopy[j] = array[j+middle+1] 
    
    i=0 #index for left  array
    j=0 #index for right array       
    while i < leftCopyIndex and j < rightCopyIndex :
        if leftCopy[i] <= rightCopy[j] :
            array[mainIndex] = leftCopy[i]
            i=i+1
        
        else:
            array[mainIndex] = rightCopy[j]
            j=j+1
        
        mainIndex = mainIndex +1         
    while i < leftCopyIndex :
        array[mainIndex] = leftCopy[i]
        i = i + 1
        mainIndex = mainIndex +1
    
    while j < rightCopyIndex :
        array[mainIndex] = rightCopy[j]
        j= j +1
        mainIndex = mainIndex +1

    print(array)    

def mergeSort(array,leftIndex,rightIndex):
    if leftIndex < rightIndex :
        middle = int((leftIndex + rightIndex)/2)
        mergeSort(array,leftIndex,middle)
        mergeSort(array,middle+1,rightIndex)
        merge(array,leftIndex,rightIndex,middle)

i=1
array = []
while i <= 10 :
    array.append(random.randint(99,999))
    i += 1

if array == [] :
    sys.exit("Array Empty\nTerminating...")

print("Original:")
print(array)
print("Passes:")
mergeSort(array, 0, 9)
print("Result:")
print(array)







