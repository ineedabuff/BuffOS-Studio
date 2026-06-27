from pathlib import Path


def test_generate_engine_exists():
    assert Path("tools/generate.py").exists()


def test_render_function_exists():
    content = Path("tools/generate.py").read_text()

    assert "def render(" in content
    assert "text.replace" in content
