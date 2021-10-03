import random,sys

def selectionSort(array, low, high) :
    for i in range(high) :
        minIndex = i
        for j in range(i+1,high) :
            if array[minIndex] > array[j] :
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i] 
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
selectionSort(array, 0, len(array))
print("Result:")
print(array)    


