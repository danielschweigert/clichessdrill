"""
Generic test methods for menu.py
"""


def menu_section_verify(menu_section: type, test_input: str, expected_valid: bool,
                        expected_message: str):
    """Test the verify method of a menu section class"""
    menu_section = menu_section(prompt_message='unit_test')
    valid_input, message = menu_section.verify(test_input)
    assert valid_input == expected_valid
    assert message == expected_message


def menu_section_show(menu_section: type, monkeypatch, test_input, expected_result):
    """Test the show method of a menu section class"""

    def fake_input(the_prompt):
        prompt_to_return_val = {
            'unit_test': test_input,
        }
        val = prompt_to_return_val[the_prompt]
        return val


    monkeypatch.setattr('builtins.input', fake_input)
    menu_section = menu_section(prompt_message='unit_test')
    result = menu_section.show()
    assert result == expected_result
