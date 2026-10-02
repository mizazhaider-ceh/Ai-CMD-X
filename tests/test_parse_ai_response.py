from helpers import load_module

mod = load_module()
parse_ai_response = mod.parse_ai_response


def test_parses_command_and_explanation():
    command, explanation, note = parse_ai_response("dir\nExplanation: Lists files and folders.")
    assert command == "dir"
    assert explanation == "Lists files and folders."
    assert note is None


def test_command_only_gives_note():
    command, explanation, note = parse_ai_response("ipconfig")
    assert command == "ipconfig"
    assert explanation == ""
    assert note is not None


def test_empty_response_is_an_error():
    command, explanation, note = parse_ai_response("\n")
    assert command is None
    assert "did not contain a command" in note


def test_malformed_second_line_still_returns_command():
    command, explanation, note = parse_ai_response("dir\nsome random text")
    assert command == "dir"
    assert note is not None
