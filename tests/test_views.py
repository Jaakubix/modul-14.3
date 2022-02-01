from main import app
from unittest.mock import Mock
import pytest

def test_homepage(monkeypatch):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    with pytest.raises('list_type'):
        with app.test_client() as client:
            response = client.get('/{list_type}')
            assert response.status_code == 200
            api_mock.assert_called_once_with('movie/{list_type}') 