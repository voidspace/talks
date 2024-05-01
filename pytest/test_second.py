

def test_app(test_client):
    response = test_client.get('/')
    breakpoint()