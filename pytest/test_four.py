import pytest
import sys
import time

@pytest.mark.skipif(sys.platform=='win32', reason="Skipped on windoze")
def test_not_windows():
    assert sys.platform != 'win32'

@pytest.mark.smoke_test
def test_core_functionality(test_client):
    def test_app(test_client):
        response = test_client.get('/healthz/live')
        assert response.status == 200

@pytest.mark.slow
def test_slow():
    time.sleep(10)
    assert True


@pytest.mark.xfail
def test_expected_failure():
    assert 3 == 2

