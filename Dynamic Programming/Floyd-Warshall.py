
def floydWarshall(distanceMatrix, pathMatrix, size):
    for k in range(size): 
        for i in range(size): 
            for j in range(size): 
                if( distanceMatrix[i][j] > (distanceMatrix[i][k]+distanceMatrix[k][j])):
                    distanceMatrix[i][j] = distanceMatrix[i][k]+distanceMatrix[k][j]
                    pathMatrix[i][j] = k+1
        print("Distance Matrix "+str(k)+":{}".format(distanceMatrix))
        print("Path Matrix "+str(k+1)+":{}".format(pathMatrix))

if __name__ == "__main__":
    distanceMatrix = []
    size = int(input("Enter Size:"))
    print("For Infinity enter 999")
    for i in range(size):  
        distanceMatrix.append([]) 
        for j in range(size):
            value = float(input("Enter Value:")) 
            if(value == 999):
                value = float('infinity')
            distanceMatrix[i].append(value) 

    print("Given Graph:{}".format(distanceMatrix))
    pathMatrix = arr = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if(distanceMatrix[i][j] != float('infinity') and distanceMatrix[i][j] != 0 ):
                pathMatrix[i][j]=i+1
    floydWarshall(distanceMatrix, pathMatrix, size)








