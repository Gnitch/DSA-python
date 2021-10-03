#   O(N*LOG(N))
import heapq

def tracePth(path,tracePath,source):
    for k in path.keys():
        val = path[k]
        if(val in path.keys()):
            if(source not in tracePath[k]):
                tracePath[k].append(path[val])
            else :
                pass
    return tracePath

def calculateDistances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    path = {vertex: 0 for vertex in graph}
    tracePath = {vertex: list() for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    heapq.heapify(pq)
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                tracePath[neighbor].append(current_vertex)
                path[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    return distances ,path, tracePath

graph = {
    '1':{'2':50,'4':10},
    '2':{'4':15,'3':10},
    '3':{'5':30},
    '4':{'1':20},
    '5':{'3':35,'2':15},
    '6':{'5':3}
}

distance , path, tracePath = calculateDistances(graph,'2')
tracePath=tracePth(path, tracePath, '2')        

print("Distances:{}".format(distance))
print("Path:{}".format(path))
print("Trace:{}".format(tracePath))





