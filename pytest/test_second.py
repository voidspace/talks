

def test_app(test_client):
    response = test_client.get('/healthz/live')
    assert response.json() == {'response': 'Healthy'}
