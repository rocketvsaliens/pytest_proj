import pytest


@pytest.fixture
def setup_collection():
    return {"vcs": "mercurial"}


@pytest.fixture
def setup_empty_collection():
    return {}
