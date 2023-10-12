import pytest
from main import Parser

@pytest.fixture
def docs():
    docs = Parser('test.md')
    return docs


def test_parser_multiple_keys(docs):
    pass




def test_parser_single_key(docs):
    pass