import networkx as nx

class MyGraph:
    def __init__(self):
        self.graph = nx.Graph()
        nodes = ['User1', 'S2', 'S3', 'S4', 'S5', 'S6', 'User2']
        self.graph.add_nodes_from(nodes)
        edges = [('User1', 'S2', {'delay': 1}), ('User1', 'S3', {'delay': 3}),
                ('S2', 'S4', {'delay': 2}), ('S3', 'S4', {'delay': 4}),
                ('S3', 'S6', {'delay': 1}), ('S4', 'S5', {'delay': 1}),
                ('S6', 'User2', {'delay': 4}), ('S5', 'User2', {'delay': 2})]
        self.graph.add_edges_from(edges)

    def get_nodes(self):
        return self.graph.nodes
    
    def get_edges(self):
        return self.graph.edges

    def DFS(self, delay, curr, target, path):
        if (delay == 0 and curr == target):
            print (path)
            return
        if (delay <= 0):
            return
        for neighbor in list(self.graph.neighbors(curr)):
            edge_delay = self.graph.edges[curr, neighbor]['delay']
            path.append((curr, neighbor))
            self.DFS(delay - edge_delay, neighbor, target, path)
            path.remove((curr, neighbor))

if __name__=="__main__":
    G = MyGraph()
    for node in G.get_nodes():
        print (node)

    for edge in G.get_edges().data():
        print (edge)

    G.DFS(6, "User1", "User2", [])

