
def test_get_data_fixture(test_client, mock_get_sf_client, config):
    mock_client = mock_get_sf_client.return_value
    mock_client.get_data.return_value = 'some data'

    result = test_client.get('/get-data?key=value')

    assert result.status_code == 200
    assert result.json() == {'result': 'some data'}

    mock_get_sf_client.assert_called_once_with(config.SF_USERNAME, config.SF_PASSWORD)
    mock_client.get_data.assert_called_once_with('value')

