from unittest.mock import Mock, patch
from core import ExactDelayPathfinder
import unittest
import networkx as nx

class TestEDPF(unittest.TestCase):

    @patch('exactdelaypathfinder.core.ExactDelayPathfinder', autospec=True)
    def test_search(self, mock_EDPF):
        '''Tests the search function'''
        new_mock_EDPF = mock_EDPF.return_value
        new_mock_EDPF.search.return_value = 42
        G = Mock()
        new_mock_EDPF.search(G, 10, 'a', 'b')
        new_mock_EDPF.search.assert_called()

    def test_small_topology_search(self):
        '''Test search function (Exact Path Algorithm) with a small-scale topology'''
        mock_EDPF = ExactDelayPathfinder()
        G = Mock()
        G = nx.Graph()
        nodes = ['User1', 'S2', 'S3', 'S4', 'S5', 'S6', 'User2']
        G.add_nodes_from(nodes)
        edges = [('User1', 'S2', {'delay': 10}), ('User1', 'S3', {'delay': 37}),
                ('S2', 'S4', {'delay': 24}), ('S3', 'S4', {'delay': 48}),
                ('S3', 'S6', {'delay': 96}), ('S4', 'S5', {'delay': 1}),
                ('S6', 'User2', {'delay': 84}), ('S5', 'User2', {'delay': 29})]

        G.add_edges_from(edges)
        mock_result = []
        mock_result = mock_EDPF.search(G, 64, 'User1', 'User2')
        mock_first_result = mock_result[0]
        mock_expected = mock_first_result.get('total_delay')
        self.assertEqual(mock_expected, 64)
