import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://dog.ceo/api", help="Url for test dog_ceo api")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
