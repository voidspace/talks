from unittest.mock import patch, AsyncMock


def test_get_data(config, test_client):
    with patch('app.get_salesforce_client', mock_class=AsyncMock) as mock_get_sf_client:
        mock_client = mock_get_sf_client.return_value
        mock_client.get_data.return_value = 'some data'

        result = test_client.get('/get-data?key=value')

        assert result.status_code == 200
        assert result.json() == {'result': 'some data'}

    mock_get_sf_client.assert_called_once_with(config.SF_USERNAME, config.SF_PASSWORD)
    mock_client.get_data.assert_called_once_with('value')


def test_get_data_fails(test_client):
    with patch('app.get_salesforce_client', mock_class=AsyncMock) as mock_get_sf_client:
        mock_client = mock_get_sf_client.return_value
        mock_client.get_data.side_effect = IOError('authentication error')

        result = test_client.get('/get-data?key=value')

        assert result.json() == {'error': 'authentication error'}
