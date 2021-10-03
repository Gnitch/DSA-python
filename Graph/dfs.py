def dfs(start_node,goal_node):
    visited = set()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)



tree = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

dfs('A','E')
