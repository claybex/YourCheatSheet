import pytest, pathlib
from main import Parser

@pytest.fixture
def docs(): 
    docs_init = Parser(f'{pathlib.Path.home()}/.config/YourCheatSheet.md')
    return docs_init

def test_parser_single_key(docs, capsys): 
    docs.get_data("GIT")
    captured = capsys.readouterr()
    assert 'Config' in captured.out

def test_parser_multiple_keys(docs, capsys):
    docs.get_data("Python","Tests")
    captured = capsys.readouterr()
    assert 'Fixture' in captured.out 