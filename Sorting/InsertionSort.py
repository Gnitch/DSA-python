import random,sys

def insertionSort(array,low,high) :
    for i in range(1,high) :
        key = array[i]
        j = i-1
        while array[j] >= key and j >= 0 :
            array[j+1] = array[j]
            j -= 1       
        
        array[j+1] = key
        print("Pass-{}:".format(i),array)

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
insertionSort(array, 0, len(array))
print("Result:")
print(array)    

