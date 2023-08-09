from utils.dicts import get_val

data = {"vcs": "mercurial"}


def test_get_val():
    assert get_val(data, "vcs") == 'mercurial'
    assert get_val(data, "vcs", "git") == 'mercurial'


empty_data = {}


def test_get_val_empty():
    assert get_val(empty_data, "vcs", "git") == 'git'
    assert get_val(empty_data, "vcs", "bazaar") == 'bazaar'

