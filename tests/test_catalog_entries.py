from pathlib import Path

ROOT = Path("installer/catalog/applications")


def test_catalog_browser_entries_exist():
    assert (ROOT / "browser" / "firefox.yaml").exists()
    assert (ROOT / "browser" / "chrome.yaml").exists()


def test_catalog_communication_entries_exist():
    assert (ROOT / "communication" / "vesktop.yaml").exists()
    assert (ROOT / "communication" / "discord.yaml").exists()


def test_catalog_entries_have_ids():
    for path in ROOT.glob("*/*.yaml"):
        text = path.read_text(encoding="utf-8")
        assert "id:" in text
        assert "name:" in text
        assert "category:" in text
