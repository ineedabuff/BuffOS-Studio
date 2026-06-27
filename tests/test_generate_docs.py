from pathlib import Path


def test_generate_docs_script_exists():
    assert Path("tools/generate_docs.py").exists()


def test_generate_docs_defines_core_documents():
    content = Path("tools/generate_docs.py").read_text()

    assert '"README.md"' in content
    assert '"VISION.md"' in content
    assert '"PRINCIPLES.md"' in content
    assert '"docs/en/README.md"' in content
    assert '"docs/fr/README.md"' in content
