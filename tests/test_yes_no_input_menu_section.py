"""
Unit test for user menu at start up
"""
import pytest
from clichessdrill.menu import YesNoInputMenuSection
from tests.menu import menu_section_verify, menu_section_show


@pytest.mark.parametrize('test_input,expected_valid,expected_message',
                         [('y', True, None), ('yes', True, None), ('bogus input', True, None),
                          ('n', True, None),
                          ])
def test_verify(test_input, expected_valid, expected_message):
    """test verify method"""
    menu_section_verify(YesNoInputMenuSection, test_input, expected_valid, expected_message)


@pytest.mark.parametrize('test_input,expected_result',
                         [('y', True), ('Yes', True), ('yes', True), ('no', False), ('n', False),
                          ('No', False), ('', False), (' ', False), ('bogus input', False)])
def test_show(monkeypatch, test_input, expected_result):
    """test show method"""
    menu_section_show(YesNoInputMenuSection, monkeypatch, test_input, expected_result)


@pytest.mark.parametrize('test_input,expected_result',
                         [('y', True), ('Yes', True), ('yes', True), ('no', False), ('n', False),
                          ('No', False), ('', False), (' ', False), ('bogus input', False)])
def test_format(test_input, expected_result):
    """test format method"""
    menu_section = YesNoInputMenuSection(prompt_message='unit_test')
    result = menu_section.format(test_input)
    assert result == expected_result
