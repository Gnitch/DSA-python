#BubbleSort using array NOT LIST
from array import*
arr = array('i',[])
len = int(input('Enter size of array:'))
for i in range(len) :
    arr.append(int(input('Enter Element:')))

print('Original array:',arr)
for i in range(len-1) :
    for j in range(len-i-1) :
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j] #Swap
   

print('Sorted Array:',arr)







