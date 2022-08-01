import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://api.openbrewerydb.org/breweries", help="Url for test openbrewerydb")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
