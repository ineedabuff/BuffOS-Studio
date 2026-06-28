from app.install_engine.report import InstallReport
from app.install_engine.report_renderer import render_report


def test_render_report():
    report = InstallReport(
        installed=["firefox"],
        skipped=["vesktop"],
        failed=["chrome"],
    )

    text = render_report(report)

    assert "Installed:" in text
    assert "firefox" in text
    assert "Skipped:" in text
    assert "vesktop" in text
    assert "Failed:" in text
    assert "chrome" in text
