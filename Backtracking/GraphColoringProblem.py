def nextVal(currvertex):
    while True:
        sol[currvertex]=(sol[currvertex]+1)%(numColors+1) #cal highest color
        if sol[currvertex] == 0:
            return 
        for i in range(numVertices):
            if adjMat[currvertex][i]!=0 and sol[currvertex] == sol[i]:
                break
        if(i==numVertices-1):
            return

def graph(currvertex):
    while True:
        nextVal(currvertex)
        if sol[currvertex] == 0:
            return
        if currvertex == numVertices-1:
            print(sol)
        else:
            graph(currvertex+1)

numVertices=int(input('Enter no. vertices:'))
sol=[0]*(numVertices)
print("Enter adjacency matrix:")
adjMat=[list(map(int,input().split())) for _ in range(numVertices)]
numColors=int(input("Enter number of colours: "))
currvertex=0
graph(currvertex)
