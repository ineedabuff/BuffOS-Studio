from app.setup.input_parser import parse_selection


def test_empty_selection():
    assert parse_selection("", 3) == []


def test_all_selection():
    assert parse_selection("a", 3) == [0, 1, 2]


def test_number_selection():
    assert parse_selection("1 3", 4) == [0, 2]


def test_comma_selection():
    assert parse_selection("1,2", 4) == [0, 1]
