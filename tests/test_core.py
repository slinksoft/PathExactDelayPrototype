from unittest.mock import Mock, patch
from core import ExactDelayPathfinder

@patch('exactdelaypathfinder.core.ExactDelayPathfinder', autospec=True)
def test_search(mock_EDPF):
    new_mock_EDPF = mock_EDPF.return_value
    new_mock_EDPF.search.return_value = 42
    G = Mock()
    new_mock_EDPF.search(G, 10, 'a', 'b')
    new_mock_EDPF.search.assert_called()