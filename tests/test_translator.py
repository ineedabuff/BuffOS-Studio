from app.i18n.translator import tr


def test_translator_returns_key():
    assert tr("analysis.start") == "analysis.start"
