import networkx as nx
import matplotlib.pyplot as plt

def create_graph(grid_size):
    G = nx.grid_2d_graph(grid_size, grid_size)
    edges = list(G.edges)
    for e in edges:
        if abs(e[0][0]-e[1][0]) > 1 or abs(e[0][1]-e[1][1]) > 1:
            G.remove_edge(*e)
    return G

def find_path(start, end, graph):
    path = nx.astar_path(graph, start, end)
    return path

def plot_graph(graph, path=None):
    pos = dict(zip(graph.nodes, graph.nodes))
    nx.draw(graph, pos, node_size=100, node_color='w')
    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='g', width=3)
    plt.show()

# Example usage
grid_size = 5
G = create_graph(grid_size)

# Add drones to the graph
drones = [
    {'start': (0, 0), 'end': (4, 4)},
    {'start': (1, 1), 'end': (2, 4)},
    {'start': (2, 0), 'end': (4, 1)}
]

# Find paths for each drone and plot the graph
for d in drones:
    path = find_path(d['start'], d['end'], G)
    plot_graph(G, path)

