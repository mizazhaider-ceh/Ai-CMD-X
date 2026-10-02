import importlib.util
import os

REPO_DIR = os.path.join(os.path.dirname(__file__), "..")


def load_module():
    path = os.path.join(REPO_DIR, "ai-cmd-x.py")
    spec = importlib.util.spec_from_file_location("ai_cmd_x", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mod = load_module()


class FakeResponse:
    def __init__(self, text):
        self.text = text


class FakeModel:
    """Stands in for the Gemini model in risk-validation tests."""
    def __init__(self, reply=None, exc=None):
        self.reply = reply
        self.exc = exc

    def generate_content(self, prompt):
        if self.exc is not None:
            raise self.exc
        return FakeResponse(self.reply)
