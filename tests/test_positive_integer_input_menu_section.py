"""
Unit test for user menu at start up
"""
import pytest
from clichessdrill.menu import PositiveIntegerInputMenuSection
from tests.menu import menu_section_verify, menu_section_show


@pytest.mark.parametrize('test_input,expected_valid,expected_message',
                         [('1', True, None),
                          ('0', False, 'positive integer number input required.'),
                          ('-1', False, 'positive integer number input required.'),
                          ('text', False, 'positive integer number input required.'),
                          ('2.5', False, 'positive integer number input required.'),
                          (None, False, 'positive integer number input required.'),
                          ])
def test_verify(test_input, expected_valid, expected_message):
    """test verify method"""
    menu_section_verify(PositiveIntegerInputMenuSection, test_input, expected_valid,
                        expected_message)


@pytest.mark.parametrize('test_input,expected_result',
                         [('3', 3), ('0', None), ('-1', None), ('3.2', None)])
def test_show(monkeypatch, test_input, expected_result):
    """test show method"""
    menu_section_show(PositiveIntegerInputMenuSection, monkeypatch, test_input, expected_result)


@pytest.mark.parametrize('test_input,expected_result', [('3', 3), ('1', 1), ])
def test_format(test_input, expected_result):
    """test format method"""
    menu_section = PositiveIntegerInputMenuSection(prompt_message='unit_test')
    result = menu_section.format(test_input)
    assert result == expected_result
