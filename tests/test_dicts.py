import pytest
from utils.dicts import get_val


@pytest.fixture
def setup_collection():
    return {"vcs": "mercurial"}


def test_get_val(setup_collection):
    assert get_val(setup_collection, "vcs") == 'mercurial'
    assert get_val(setup_collection, "vcs", "svn") == 'mercurial'
    assert get_val(setup_collection, "bazaar") == 'git'
    assert get_val({}, "bazaar", "python") == 'python'
