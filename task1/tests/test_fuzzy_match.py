from utils import map_headers

def test_fuzzy_map():
    headers = ['amt', 'desc', 'acct', 'dt']
    expected = ['amount', 'description', 'account', 'date']
    mapping = map_headers(headers, expected)
    assert set(mapping.values()) == set(expected)
