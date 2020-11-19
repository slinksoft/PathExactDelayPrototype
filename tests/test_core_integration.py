from core import ExactDelayPathfinder
import unittest
import networkx as nx

class TestEDPF(unittest.TestCase):
        
    def test_small_topology_search(self):
        """ Test search function (Exact Path Algorithm) with a small-scale topology """
        EDPF = ExactDelayPathfinder()
        G = nx.Graph()
        
        # The following is a small-scale topology we will use to test the
        # algorithm's functionality and correctness. Modifying the nodes and edges (links)
        # of the graph (topology) will affect the outcome of the test which may result in a failure.
        nodes = ['User1', 'S2', 'S3', 'S4', 'S5', 'S6', 'User2']
        G.add_nodes_from(nodes)
        edges = [('User1', 'S2', {'delay': 10}), ('User1', 'S3', {'delay': 37}),
                ('S2', 'S4', {'delay': 24}), ('S3', 'S4', {'delay': 48}),
                ('S3', 'S6', {'delay': 96}), ('S4', 'S5', {'delay': 1}),
                ('S6', 'User2', {'delay': 84}), ('S5', 'User2', {'delay': 29})]

        G.add_edges_from(edges)

        # Create result variables and run the test search
        result = []
        result = EDPF.search(G, 64, 'User1', 'User2')
        first_result = result[0]
        expected = first_result.get('total_delay') # extract first result
        # The first result should be an exact path with delay of 64
        self.assertEqual(expected, 64)
        
    def test_large_topology_search(self):
        """ Test search function (Exact Path Algorithm) with a large-scale topology """
        EDPF = ExactDelayPathfinder()
        G = nx.Graph()
        
        # The following is a large-scale topology we will use to test the
        # algorithm's functionality and correctness. Modifying the nodes and edges (links)
        # of the graph (topology) will affect the outcome of the test which may result in a failure.
        nodes = ['User1', 'S2', 'S3', 'S4', 'S5', 'S6','S7','S8','S9','S10', 'User2']
        G.add_nodes_from(nodes)
        edges = [('User1', 'S2', {'delay': 10}), ('User1', 'S3', {'delay': 37}),
                ('S2', 'S4', {'delay': 24}), ('S3', 'S4', {'delay': 48}),
                ('S3', 'S6', {'delay': 96}), ('S4', 'S5', {'delay': 1}),
                ('S6', 'User2', {'delay': 84}), ('S5', 'User2', {'delay': 29}),
                ('S6', 'S8', {'delay': 25}),('S10', 'S9', {'delay': 66}),
                ('S7', 'S8', {'delay': 92}),('S9', 'S4', {'delay': 50}),
                ('S2', 'S10', {'delay': 36}),('S9', 'User2', {'delay': 75}),
                ('S8', 'User2', {'delay': 96}),('User2', 'S2', {'delay': 81}),
                ('S1', 'S10', {'delay': 24}),('S10', 'User2', {'delay': 140})]

        G.add_edges_from(edges)

        # Create result variables and run the test search
        result = []
        result = EDPF.search(G, 120, 'User1', 'User2')
        first_result = result[0]
        expected = first_result.get('total_delay') # extract first result
        # The first result should be a close path with delay of 115
        self.assertEqual(expected, 115)
        second_result = result[1]
        expected2 = second_result.get('total_delay')
        # Second closest result should be 91
        self.assertEqual(expected2, 91)
        
    def test_no_path_search(self):
        """ Test search function (Exact Path Algorithm) with a with no possible path
            between the starting node and the target node
        """
        EDPF = ExactDelayPathfinder()
        G = nx.Graph()
        
        # The following is a small-scale topology we will use to test the
        # algorithm's functionality and correctness. Modifying the nodes and edges (links)
        # of the graph (topology) will affect the outcome of the test which may result in a failure.
        nodes = ['User1', 'S2', 'S3', 'S4', 'S5', 'S6', 'User2']
        G.add_nodes_from(nodes)
        edges = [('User1', 'S2', {'delay': 10}), ('User1', 'S3', {'delay': 37}),
                ('S2', 'S4', {'delay': 24}), ('S3', 'S4', {'delay': 48}),
                ('S3', 'S6', {'delay': 96}), ('S4', 'S5', {'delay': 1}),
                ('S6', 'S3', {'delay': 84}), ('S5', 'S6', {'delay': 29})]

        G.add_edges_from(edges)

        # Create result variables and run the test search
        result = []
        result = EDPF.search(G, 128, 'User1', 'User2')
        # The first result should be an empty list due to no possible path
        # between User1 and User2
        self.assertEqual(result, [])
