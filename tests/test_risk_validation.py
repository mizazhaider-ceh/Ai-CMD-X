from helpers import FakeModel, load_module

mod = load_module()


def check(reply=None, exc=None):
    mod.model = FakeModel(reply=reply, exc=exc)
    return mod.validate_command_risk("del /f /s /q C:\\*")


def test_safe_command_returns_none():
    assert check(reply="Safe") is None


def test_risky_command_returns_explanation():
    result = check(reply="Risky: Permanently deletes files without confirmation.")
    assert result == "Permanently deletes files without confirmation."


def test_unexpected_reply_is_treated_as_risky():
    result = check(reply="maybe, who knows?")
    assert result is not None
    assert "unexpected" in result.lower()


def test_empty_reply_is_treated_as_risky():
    result = check(reply="")
    assert result is not None
    assert "risky" in result.lower()


def test_api_error_is_treated_as_risky():
    result = check(exc=RuntimeError("boom"))
    assert result is not None
    assert "Risk check failed" in result


def test_empty_command_is_treated_as_risky():
    mod.model = FakeModel(reply="Safe")
    assert mod.validate_command_risk("") is not None
