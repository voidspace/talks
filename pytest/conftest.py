from app import create_app

import pytest

@pytest.fixture
def test_client(event_loop):
    app = create_app()
    return app.test_client()
