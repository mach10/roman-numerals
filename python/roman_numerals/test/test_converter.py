import pytest

from roman_numerals import converter


@pytest.fixture
def undertest():
    return converter.Converter()


def test_converts_one(undertest):
    result = undertest.convert(1)
    assert 'I' == result

