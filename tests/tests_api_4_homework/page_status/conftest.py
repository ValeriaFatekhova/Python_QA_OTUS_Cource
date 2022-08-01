import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru", help="Url for test")
    parser.addoption("--status_code", default="200", help="Expexted status code for request")


@pytest.fixture(scope="function")
def url(request):
    yield request.config.getoption("--url")


@pytest.fixture(scope="function")
def status_code(request):
    yield request.config.getoption("--status_code")
