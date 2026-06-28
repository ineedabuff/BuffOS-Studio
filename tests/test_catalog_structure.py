from pathlib import Path

ROOT = Path("installer/catalog")


def test_catalog_main_folders_exist():
    for folder in [
        "applications",
        "bundles",
        "profiles",
        "hardware",
        "desktop",
        "distributions",
    ]:
        assert (ROOT / folder).is_dir()


def test_catalog_application_categories_exist():
    for folder in [
        "browser",
        "communication",
        "music",
        "gaming",
        "development",
        "ai",
        "terminal",
        "graphics",
        "video",
        "office",
        "privacy",
        "system",
    ]:
        assert (ROOT / "applications" / folder).is_dir()
