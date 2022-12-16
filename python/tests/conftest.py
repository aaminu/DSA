import pytest


def country_code_checker(node: dict, key: str, value: any):
    if node.get(key) == value:
        return True
    return False


@pytest.fixture(scope="module")
def test_validator():
    return country_code_checker
