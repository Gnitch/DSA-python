def bfs(start_node,goal_node):
    visited = []
    queue = []
    path_cost = 1
    visited.append(start_node)
    queue.append(start_node)

    while queue :
        node = queue.pop(0)
        print(node,end=' ')
        if(node == goal_node):
            break

        for neighbor in tree[node]:
            if neighbor not in visited :
                path_cost += 1
                visited.append(neighbor)
                queue.append(neighbor)

    print()
    print('Path cost:',path_cost)



tree = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

bfs('A','E')
