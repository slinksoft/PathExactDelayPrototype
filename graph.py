import networkx as nx

class MyGraph:
    def __init__(self):
        self.graph = nx.Graph()
        nodes = ['User1', 'S2', 'S3', 'S4', 'S5', 'S6', 'User2']
        self.graph.add_nodes_from(nodes)
        edges = [('User1', 'S2', {'delay': 10}), ('User1', 'S3', {'delay': 37}),
                ('S2', 'S4', {'delay': 24}), ('S3', 'S4', {'delay': 48}),
                ('S3', 'S6', {'delay': 96}), ('S4', 'S5', {'delay': 1}),
                ('S6', 'User2', {'delay': 84}), ('S5', 'User2', {'delay': 29})]
        self.graph.add_edges_from(edges)
        self._result = {}

    def get_nodes(self):
        return self.graph.nodes
    
    def get_edges(self):
        return self.graph.edges

    def DFS(self, total_delay, start, end, error):
        '''Obtain paths with total delays equal or close to the user's requirements.'''
        visits = {}
        for node in G.get_nodes():
            visits[str(node)] = 0

        visits[start] = 1

        self._DFS2(total_delay, start, end, [], error, visits)
        print(visits)
        return self._result

    def _DFS2(self, delay, curr, target, path, error, visits):
        print(path)
        print("----------------")
        if (-error <= delay <= error and curr == target and path != []):
            print("FOUND")
            key = abs(delay) # The target was reached
            if key in self._result:
                self._result[key].append(path.copy()) # Path must be copied or else it will get erased
            else:
                self._result[key] = [path.copy()]
            return
        if (delay <= -error):
            print("NOPE")
            return # A dead end was reached
        for neighbor in list(self.graph.neighbors(curr)):
            if (visits[str(neighbor)] < 3):
                visits[str(neighbor)] += 1
                edge_delay = self.graph.edges[curr, neighbor]['delay']
                path.append((curr, neighbor)) # Found a potential path with this as the starting edge
                self._DFS2(delay - edge_delay, neighbor, target, path, error, visits)
                path.remove((curr, neighbor)) # Clean up after an end was reached (target or dead end)
                visits[str(neighbor)] -= 1

if __name__=="__main__":
    G = MyGraph()
    for node in G.get_nodes():
        print (node)

    for edge in G.get_edges().data():
        print (edge)

    result = G.DFS(total_delay=350, start="User1", end="S4", error=2)

    for off_by, paths in result.items():
        print(f"Paths with delay off by {off_by}:")
        for path in paths:
            print(f"| {path}")
