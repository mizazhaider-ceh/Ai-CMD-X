from helpers import load_module

mod = load_module()


def test_loads_valid_aliases(tmp_path):
    alias_file = tmp_path / ".px_aliases"
    alias_file.write_text("ip=show my IP address\n# a comment\nlogs=dir C:\\logs\n")
    aliases = mod.load_aliases(str(alias_file))
    assert aliases == {"ip": "show my IP address", "logs": "dir C:\\logs"}


def test_skips_bad_lines(tmp_path):
    alias_file = tmp_path / ".px_aliases"
    alias_file.write_text("no-equals-sign-here\n=empty-name\nok=dir\n")
    aliases = mod.load_aliases(str(alias_file))
    assert aliases == {"ok": "dir"}


def test_missing_file_returns_empty_dict(tmp_path):
    assert mod.load_aliases(str(tmp_path / "does-not-exist")) == {}
