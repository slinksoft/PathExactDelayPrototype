from unittest.mock import Mock, patch
from core import ExactDelayPathfinder
from unittest import TestCase
import networkx as nx

class TestEDPF(TestCase):
        
    @patch.object(ExactDelayPathfinder, '_search')
    def test_search(self, mock_search):
        """ Test the _search function, the DFS algorithm (recursive method)."""
        new_EDPF = ExactDelayPathfinder()
        mock_search.return_value = []

        G = Mock()
        G.nodes = []
        delay = 64;
        start = 'a'
        end = 'b'
        new_EDPF.search(G, 64, 'a', 'b')
        new_EDPF._search.assert_called()

    def test_search_graph_Error(self):
        """Test the search function attribute errors for the graph input parameter."""
        EDPF = ExactDelayPathfinder()
        G = None
        self.assertRaises(AttributeError, EDPF.search, G, 10,'a', 'b')
    
    def test_search_delay_Error(self):
        """Test the search function attribute errors for the delay input parameter."""
        EDPF = ExactDelayPathfinder()
        G = Mock()
        self.assertRaises(AttributeError, EDPF.search, G, -10,'a', 'b')
    
    def test_search_max_result_Error(self):
        """Tests the search function attribute errors for the max result parameter."""
        EDPF = ExactDelayPathfinder()
        G = Mock()
        self.assertRaises(AttributeError, EDPF.search, G, 10,'a', 'b', -5)
            
    def test_small_topology_search(self):
        """Test search function (Exact Path Algorithm) with a small-scale topology."""
        mock_EDPF = ExactDelayPathfinder()
        G = Mock()
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
        mock_result = []
        mock_result = mock_EDPF.search(G, 64, 'User1', 'User2')
        mock_first_result = mock_result[0]
        mock_expected = mock_first_result.get('total_delay') # extract first result
        # The first result should be an exact path with delay of 64
        self.assertEqual(mock_expected, 64)
