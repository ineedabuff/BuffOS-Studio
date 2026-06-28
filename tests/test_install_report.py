from app.install_engine.report import InstallReport


def test_install_report_success():
    report = InstallReport(
        installed=["firefox"],
        skipped=[],
        failed=[],
    )

    assert report.success


def test_install_report_failure():
    report = InstallReport(
        installed=[],
        skipped=[],
        failed=["firefox"],
    )

    assert not report.success
