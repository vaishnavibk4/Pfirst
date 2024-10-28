def dfs(g,start):
    stack = [start]
    visited = set()
    track = []


    while stack:
        current = stack.pop()


        if current not in visited:
            visited.add(current)
            print(visited)
            print(f"curr {current}")

        

        for nieghbours in g[current]:
            print(nieghbours)
            if nieghbours not in visited:
                stack.append(nieghbours)
                print(stack)

        print("vis",visited)        

    
    return track




graph = {
    1:[2,3,4],
    2:[1,5],
    3:[1,5],
    4:[1,5],
    5:[2,3,4]
}

print(dfs(graph,1))