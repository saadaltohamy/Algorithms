# Minimum Spanning Tree(MST) using Kruskal's algorithm


# find function
def find(parent, i):
    # if parent of the vertex is itself, then return the vertex
    if parent[i] == i:
        return i
    
    # else, recursively call find function on the parent of the vertex
    return find(parent, parent[i])

# union function
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[yroot] > rank[xroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# kruskal function
def kruskal(graph, V, E):

    # First: initialization process:

    result = []     # Minimum Spanning Tree(MST) result of the algorithm
    i = 0           # traverse the edges of original graph in Line 46
    e = 0           # number of edges included in the MST
    parent = []     # parent of each vertex in the disjoint set data structure
    rank = []       # rank of each vertex in the disjoint set data structure
    # initially, parent of each vertex is itself, and rank is 0
    for node in range(V):
        parent.append(node)
        rank.append(0)


    # Second: sort the graph in ascending order based on weight:
    graph = sorted(graph, key=lambda item: item[2])


    # Third: pick the smallest edge and check if it forms a cycle with the spanning tree formed so far:
    while e < V - 1:      # MST has V - 1 edges
        u, v, w = graph[i]
        i += 1

        # find the group of u and v
        x = find(parent, u)
        y = find(parent, v)

        # if u and v don't belong to the same group, then union them and add the edge to the MST
        # and if they belong to the same group, then ignore the edge and continue
        if x != y:
            union(parent, rank, x, y)
            result.append([u, v, w])
            e += 1


    # Finally, print the edges of the MST:
    print("Following are the edges in the constructed MST")
    for u, v, weight in result:
        print("%d -- %d == %d" % (u, v, weight))


# main function
def main():
    V = 4
    E = 5
    graph = []
    
    # add edges to the graph (node1, node2, weight)
    graph.append([0, 1, 10])
    graph.append([0, 2, 6])
    graph.append([0, 3, 5])
    graph.append([1, 3, 15])
    graph.append([2, 3, 4])
    kruskal(graph, V, E)

if __name__ == '__main__':
    main()