import networkx as nx
import matplotlib.pyplot as plt

# Create the graph
G = nx.Graph()

# Add edges with weights
edges = [
    ('A', 'B', 2),
    ('A', 'D', 4),
    ('B', 'C', 3),
    ('B', 'D', 2),
    ('B', 'E', 6),
    ('C', 'F', 1),
    ('D', 'G', 3),
    ('E', 'G', 1),
    ('E', 'H', 5),
    ('F', 'H', 2),
]

G.add_weighted_edges_from(edges)

# Apply Dijkstra's algorithm (e.g., from A to F)
path = nx.dijkstra_path(G, source='A', target='F', weight='weight')
distance = nx.dijkstra_path_length(G, source='A', target='F', weight='weight')

print("Shortest path from A to F:", path)
print("Total distance:", distance)

# Node positions for visualization
pos = {
    'A': (0, 2),
    'B': (1, 2.5),
    'C': (2.5, 2.5),
    'D': (0.5, 1),
    'E': (1.5, 1.5),
    'F': (3, 1.5),
    'G': (1, 0.2),
    'H': (2.2, 0.5),
    'I': (3.5, 2.8),   # Right of 'C'
    'J': (2, 3.2),     # Above 'C'
    'K': (0.2, 3.2),   # Above 'A'
    'L': (-0.5, 1.5),  # Left of 'D'
    'M': (3.8, 0.8),   # Right of 'F' and above 'H'
    'N': (2.8, -0.3),  # Below 'H'
    'O': (0.5, -0.5),  # Below 'G'
    'P': (-0.5, 0.5),  # Left of 'G'
    'Q': (1.8, -0.8),  # Bottom right corner
}

# Add more edges to connect the new nodes
additional_edges = [
    ('C', 'I', 2),
    ('C', 'J', 2),
    ('A', 'K', 3),
    ('D', 'L', 2),
    ('F', 'M', 2),
    ('H', 'M', 2),
    ('H', 'N', 2),
    ('G', 'O', 2),
    ('G', 'P', 2),
    ('H', 'Q', 3),
]

G.add_weighted_edges_from(additional_edges)

# Draw graph
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=12)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

# Highlight the shortest path
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

plt.title("Dijkstra's Shortest Path from A to F")
plt.show()
