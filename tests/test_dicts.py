import pytest
from utils.dicts import get_val


@pytest.mark.parametrize("key, default, expected", [
    ("vcs", None, "mercurial"),
    ("vcs", "git", "mercurial"),
    ("bazaar", "git", "git"),
])
def test_get_val(setup_collection, key, default, expected):
    assert get_val(setup_collection, key, default) == expected


@pytest.mark.parametrize("key, default, expected", [
    ("vcs", "git", "git"),
    ("vcs", "bazaar", "bazaar"),
])
def test_get_val_empty(setup_empty_collection, key, default, expected):
    assert get_val(setup_empty_collection, key, default) == expected
