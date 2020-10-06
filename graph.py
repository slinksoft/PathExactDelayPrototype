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

    def DFS(self, total_delay, start, end):
        '''Obtain paths with total delays equal to the user's requirements.'''
        return self._DFS2(total_delay, start, end, [], 10)

    def _DFS(self, delay, curr, target, path):
        if (delay == 0 and curr == target):
            print (path) # The target was reached
            return
        if (delay <= 0):
            return # A dead end was reached
        for neighbor in list(self.graph.neighbors(curr)):
            edge_delay = self.graph.edges[curr, neighbor]['delay']
            path.append((curr, neighbor)) # Found a potential path with this as the starting edge
            self._DFS(delay - edge_delay, neighbor, target, path)
            path.remove((curr, neighbor)) # Clean up after an end was reached (target or dead end)

    def _DFS2(self, delay, curr, target, path, error):
        if (-error <= delay <= error and curr == target):
            print (path)
            print ("| off by: " + str(abs(delay))) # The target was reached
            return
        if (delay <= -error):
            return # A dead end was reached
        for neighbor in list(self.graph.neighbors(curr)):
            edge_delay = self.graph.edges[curr, neighbor]['delay']
            path.append((curr, neighbor)) # Found a potential path with this as the starting edge
            self._DFS2(delay - edge_delay, neighbor, target, path, error)
            path.remove((curr, neighbor)) # Clean up after an end was reached (target or dead end)

if __name__=="__main__":
    G = MyGraph()
    for node in G.get_nodes():
        print (node)

    for edge in G.get_edges().data():
        print (edge)

    G.DFS(total_delay=8, start="User1", end="User1")
