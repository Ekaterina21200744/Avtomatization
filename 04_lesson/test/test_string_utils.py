import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("питон", "Питон"),
])

def test_capitalize_positive(input_str, expected):
    result = string_utils.capitalize(input_str)
    assert result == expected, f"Ожидалось: '{expected}', получено: '{result}'"

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("               hello world", "hello world")
])

def test_trim_pozitive(input_str, expected):
    assert string_utils.trim(input_str) ==expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S",True ),
    ("Skyeng", "e", True),
    ("", "к", False)
])
def test_contains_pozitive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) ==expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str,  symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Sky", "Pro")
])
def test_cdelete_symbol_pozitive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) ==expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" ", " "),
    ("", ""),
    ( "\t", "\t"),
])
def test_trim_negative (input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "a",False ),
    ("Skyeng", "K", False),
    ("", "ф", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) ==expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str,  symbol, expected", [
    ("SkyPro", "", "SkyPro"),
    ("test", "", "test"),
    ("Скайпро", "z", "Скайпро")
])
def test_cdelete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) ==expected