from click.testing import CliRunner

def test_bake_project(cookies):
    runner = CliRunner()
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()
