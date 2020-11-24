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
        
    @patch.object(ExactDelayPathfinder, '_search')
    def test_search(self, mock_search):
        """ Tests the _search function, the DFS algorithm (recursive method) 
        
            Parameters:
               mock_EDPF: Mock object reference of ExactDelayPathfinder
        """
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
        """ Tests the search function attribute errors for the graph input parameter """
        EDPF = ExactDelayPathfinder()
        G = None
        self.assertRaises(AttributeError, EDPF.search, G, 10,'a', 'b')
        
    
    def test_search_delay_Error(self):
        """ Tests the search function attribute errors for the delay input parameter """
        EDPF = ExactDelayPathfinder()
        G = Mock()
        self.assertRaises(AttributeError, EDPF.search, G, -10,'a', 'b')
    
    def test_search_max_result_Error(self):
        """ Tests the search function attribute errors for the max result parameter """
        EDPF = ExactDelayPathfinder()
        G = Mock()
        self.assertRaises(AttributeError, EDPF.search, G, -10,'a', 'b', -5)

