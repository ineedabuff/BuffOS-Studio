from pathlib import Path


def test_generators_package_exists():
    assert Path("installer/app/generators").exists()
    assert Path("installer/app/generators/engine.py").exists()


def test_generator_templates_exist():
    assert Path("installer/app/generators/templates/plugin/plugin.py.j2").exists()
