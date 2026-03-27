import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, end):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    node = end

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    return dist[end], path


# -------- INPUT --------

locations = input("Enter locations (space separated): ").split()
graph = {loc: [] for loc in locations}

roads = int(input("Enter number of roads: "))

edges = []

for i in range(roads):
    u, v, w = input("Enter road (From To Distance): ").split()
    w = int(w)

    graph[u].append((v, w))
    graph[v].append((u, w))
    edges.append((u, v, w))


start = input("Enter start location: ")
end = input("Enter destination: ")

distance, path = dijkstra(graph, start, end)

# -------- PRINT OUTPUT --------

print("\nGraph Connections:")
for node in graph:
    print(node, "->", graph[node])

print("\nShortest Path:", " -> ".join(path))
print("Total Distance:", distance)


# -------- DRAW GRAPH --------

G = nx.Graph()

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_size=2000)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Highlight shortest path
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3)

plt.title("Traffic Route Graph with Shortest Path")
plt.show()