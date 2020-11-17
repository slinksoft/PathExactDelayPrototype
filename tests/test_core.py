from unittest.mock import Mock, patch
from core import ExactDelayPathfinder
import unittest
import networkx as nx

class TestEDPF(unittest.TestCase):

    @patch('exactdelaypathfinder.core.ExactDelayPathfinder', autospec=True)
    def test_search(self, mock_EDPF):
        """ Tests the search function 
        
            Parameters:
               mock_EDPF: Mock object reference of ExactDelayPathfinder
        """
        new_mock_EDPF = mock_EDPF.return_value
        new_mock_EDPF.search.return_value = 42
        G = Mock()
        new_mock_EDPF.search(G, 10, 'a', 'b')
        new_mock_EDPF.search.assert_called()
        
    @patch('exactdelaypathfinder.core.ExactDelayPathfinder', autospec=True)
    def test_search(self, mock_EDPF):
        """ Tests the _search function, the DFS algorithm (recursive method) 
        
            Parameters:
               mock_EDPF: Mock object reference of ExactDelayPathfinder
        """
        new_mock_EDPF = mock_EDPF.return_value
        new_mock_EDPF._search.return_value = 86
        G = Mock()
        delay = 64;
        start = 'a'
        end = 'b'
        new_mock_EDPF._search(G, 64, 'a', 'b', [])
        new_mock_EDPF._search.assert_called_with(G, delay, start, end, visits=[])

    @patch('exactdelaypathfinder.core.ExactDelayPathfinder', autospec=True)
    def test_search_graph_Error(self, mock_EDPF):
        """ Tests the search function attribute errors for the graph input parameter 
        
            Parameters:
               mock_EDPF: Mock object reference of ExactDelayPathfinder
        """
        new_mock_EDPF = ExactDelayPathfinder()
        G = None
        self.assertRaises(AttributeError, new_mock_EDPF.search, G, 10,'a', 'b')
        
    
    @patch('exactdelaypathfinder.core.ExactDelayPathfinder', autospec=True)
    def test_search_delay_Error(self, mock_EDPF):
        """ Tests the search function attribute errors for the delay input parameter 
        
            Parameters:
               mock_EDPF: Mock object reference of ExactDelayPathfinder
        """
        new_mock_EDPF = ExactDelayPathfinder()
        G = Mock()
        self.assertRaises(AttributeError, new_mock_EDPF.search, G, -10,'a', 'b')
    
    @patch('exactdelaypathfinder.core.ExactDelayPathfinder', autospec=True)
    def test_search_max_result_Error(self, mock_EDPF):
        """ Tests the search function attribute errors for the max result parameter 
        
            Parameters:
               mock_EDPF: Mock object reference of ExactDelayPathfinder
        """
        new_mock_EDPF = ExactDelayPathfinder()
        G = Mock()
        self.assertRaises(AttributeError, new_mock_EDPF.search, G, -10,'a', 'b', -5)
            
    def test_small_topology_search(self):
        """ Test search function (Exact Path Algorithm) with a small-scale topology """
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
