from app import create_app
from app.config import Config

import pytest

from unittest.mock import patch, AsyncMock

@pytest.fixture
def app(event_loop):
    return create_app()

@pytest.fixture
def test_client(app):
    return app.test_client()

@pytest.fixture
def config():
    return Config


@pytest.fixture
def mock_get_sf_client():
    with patch('app.get_salesforce_client', mock_class=AsyncMock) as mock_get_sf_client:
        yield mock_get_sf_client

# Magic to switch off slow tests by default
# Unless you pass --runslow


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
