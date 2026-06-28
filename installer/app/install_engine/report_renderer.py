from __future__ import annotations

from app.install_engine.report import InstallReport


def render_report(report: InstallReport) -> str:
    lines = [
        "Install Report",
        "--------------",
    ]

    if report.installed:
        lines.append("Installed:")
        lines.extend(f"  ✓ {item}" for item in report.installed)

    if report.skipped:
        lines.append("Skipped:")
        lines.extend(f"  - {item}" for item in report.skipped)

    if report.failed:
        lines.append("Failed:")
        lines.extend(f"  ✗ {item}" for item in report.failed)

    return "\n".join(lines)
