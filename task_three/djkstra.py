import heapq

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

def dijkstra(graph, start):
    distances = {}
    heap = [(0, start)]

    while heap:
        distance, node = heapq.heappop(heap)
        
        if node in distances:
            continue

        distances[node] = distance
        
        for neighbor, weight in graph[node].items():
            if neighbor not in distances:
                heapq.heappush(heap, (distance + weight, neighbor))
    
    return distances

distances = dijkstra(graph, 'A')

for node, distance in distances.items():
    print(f'Distance to vertex {node} is {distance}')
