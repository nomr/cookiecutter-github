import pytest
from click.testing import CliRunner
from git import Repo

@pytest.fixture
def cookie(cookies):
    return cookies.bake()


@pytest.fixture
def repo(cookie):
    return Repo(cookie.project)


def test_project_created(cookie):
    assert cookie.exit_code == 0
    assert cookie.exception is None
    assert cookie.project.isdir()


def test_setup_git(repo):
    assert not repo.bare
    assert len(repo.untracked_files) == 0

    branch_names = [ x.name for x in repo.branches ]
    assert 'master' in branch_names
    assert 'ck/template' in branch_names

    tag_names = [ x.name for x in repo.tags ]
    assert '0.1.0' in tag_names
