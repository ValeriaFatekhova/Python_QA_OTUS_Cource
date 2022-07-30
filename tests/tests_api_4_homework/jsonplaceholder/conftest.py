import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://jsonplaceholder.typicode.com/posts", help="Url for test jsonplaceholder api")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
