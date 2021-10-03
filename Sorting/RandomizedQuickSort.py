import random,sys

def quickSort(array, lowerBound, higherBound) :
    if lowerBound < higherBound :
        pivot = partitionrand(array , lowerBound, higherBound)
        quickSort(array, lowerBound, pivot -1)
        quickSort(array, pivot +1, higherBound)

def partitionrand(array , lowerBound, higherBound): 
  
    randpivot = random.randrange(lowerBound, higherBound) 
    array[lowerBound], array[randpivot] = array[randpivot], array[lowerBound] 
    return partition(array, lowerBound, higherBound) 

def partition(array, lowerBound, higherBound) :
    low = lowerBound
    high = higherBound
    element = array[lowerBound]
    while low < high :
        while array[low] <= element and low < high :
            low += 1
        
        while array[high] > element :
            high -=  1
        
        if low < high : #checking index
            array[low], array[high] = array[high], array[low] #Swap

    array[lowerBound] = array[high]
    array[high] = element
    print(array)
    return high

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
quickSort(array, 0, 9)
print("Result:")
print(array)    

