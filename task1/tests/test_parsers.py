from parsers.comma_parser import Parser

def test_parser():
    p = Parser()
    data = p.parse('samples/data.csv')
    assert isinstance(data, list)
