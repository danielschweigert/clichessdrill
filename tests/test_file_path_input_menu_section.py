"""
Unit test for user menu at start up
"""
import os
import pytest
from clichessdrill.menu import FilePathInputMenuSection
from tests.menu import menu_section_verify, menu_section_show

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_GAME_PLAN = os.path.join(THIS_DIR, 'data', 'game_plans', 'test-default.json')
CUSTOM_GAME_PLAN = os.path.join(THIS_DIR, 'data', 'game_plans', 'test-default.json')
NON_EXISTENT_GAME_PLAN = os.path.join(THIS_DIR, 'data', 'game_plans', 'test_not_exist.json')
NOT_JSON_FILE = os.path.join(THIS_DIR, 'data', 'game_plans', 'test-default')


@pytest.mark.parametrize('test_input,expected_valid,expected_message',
                         [(DEFAULT_GAME_PLAN, True, None),
                          (CUSTOM_GAME_PLAN, True, None),
                          (NON_EXISTENT_GAME_PLAN, False,
                           'File path to existing json file required.'),
                          (NOT_JSON_FILE, False, 'File path to existing json file required.'),
                          ])
def test_verify(test_input, expected_valid, expected_message):
    """test verify method"""
    menu_section_verify(FilePathInputMenuSection, test_input, expected_valid, expected_message)


@pytest.mark.parametrize('test_input,expected_result',
                         [(DEFAULT_GAME_PLAN, DEFAULT_GAME_PLAN),
                          (CUSTOM_GAME_PLAN, DEFAULT_GAME_PLAN),
                          (NON_EXISTENT_GAME_PLAN, None),
                          (NOT_JSON_FILE, None),
                          ])
def test_show(monkeypatch, test_input, expected_result):
    """test show method"""
    menu_section_show(FilePathInputMenuSection, monkeypatch, test_input, expected_result)


@pytest.mark.parametrize('test_input,expected_result',
                         [(DEFAULT_GAME_PLAN, DEFAULT_GAME_PLAN),
                          (CUSTOM_GAME_PLAN, DEFAULT_GAME_PLAN)])
def test_format(test_input, expected_result):
    """test format method"""
    menu_section = FilePathInputMenuSection(prompt_message='unit_test')
    result = menu_section.format(test_input)
    assert result == expected_result
