import heapq


# dijkstra algorithm
def dijkstra(graph, start):
    # Initialize distances to infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a priority queue to store nodes and their distances
    pq = [(distances[node], node) for node in graph]

    # Initialize the shortest path and previous node dictionaries
    previous = {}

    while pq:
        # Get the node with the minimum distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)

        # Skip if the current distance is greater than the stored distance
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # update the priority queue
                for i, (dist, node) in enumerate(pq):
                    if node == neighbor:
                        pq[i] = (distance, node)
                        break
                heapq.heapify(pq)
                previous[neighbor] = current_node

    return distances, previous


def shortest_path(distances, previous, start, end):
    # Backtrack from the end node to the source node to construct the shortest path
    path = {}
    end_node = end
    current_node = end_node
    while current_node != start:
        path[current_node] = previous[current_node]
        current_node = previous[current_node]

    # Reverse the shortest path and add the start node
    path = [start] + list(reversed(path.keys()))
    return path


# Example usage
graph = {
    'A': {'B': 2, 'C': 4, 'D': 1},
    'B': {'A': 2, 'C': 1, 'E': 3},
    'C': {'A': 4, 'B': 1, 'D': 2, 'E': 5},
    'D': {'A': 1, 'C': 2, 'F': 4},
    'E': {'B': 3, 'C': 5, 'F': 2},
    'F': {'D': 4, 'E': 2}
}


start_node = 'A'
distances, previous = dijkstra(graph, start_node)
print(shortest_path(distances, previous, start_node, 'C'))
