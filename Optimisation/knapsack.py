'''
Complexity:o(nlogn)
'''
def knapsack(cost, weight, sizeKnap, arrayFinal, numElements):
    knapWeight = sizeKnap
    for i in range(numElements):
        if weight[i] > knapWeight :
            break
        arrayFinal[i] = 1.0 
        knapWeight = knapWeight - weight[i]
    if i <= numElements :
        arrayFinal[i] = knapWeight/weight[i]        
    sum = 0.0
    print("Weight:{}".format(weight))
    print("Cost:{}".format(cost))
    print("Final Array:{}".format(arrayFinal))
    for i in range(numElements):
        sum += cost[i] * arrayFinal[i]

    return sum


numElements = int(input("Enter size of elements:"))
sizeKnap = float(input("Enter size for knapsack:"))
cost = []
weight = []
divideSort = []
for i in range(numElements):
    cost.append(float(input("Enter cost:")))
    weight.append(float(input("Enter weight:")))

for i in range(numElements):
    divideSort.append(cost[i]/weight[i])

finalSort = []
for i in range(numElements):
    finalSort.append(tuple([cost[i],weight[i],divideSort[i]]))

# finalSort.sort(key )
sortedArr = sorted(finalSort, key=lambda x: x[-1],reverse=True)

print(sortedArr)
arrayFinal = []
arrayFinal = [0] * numElements
# print("Divide-Sort",divideSort)
#quickSort(divideSort, cost, weight, 0, len(divideSort)-1)
newCost = []
newWeight = []
for i in range(len(sortedArr)):
    temp = sortedArr[i]
    newCost.append(temp[0])
    newWeight.append(temp[1])
# print(newCost)
# print(newWeight)
total =  knapsack(newCost, newWeight, sizeKnap, arrayFinal, numElements)
print("Total:{}".format(total))





