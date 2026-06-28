from __future__ import annotations

from app.checks.result import CheckResult


def render_check(result: CheckResult) -> str:
    symbol = "✓" if result.passed else "✗"
    return f"{symbol} {result.title}"


def render_report(results: list[CheckResult]) -> str:
    lines = [
        "Buff Ready",
        "----------",
    ]

    for result in results:
        lines.append(render_check(result))

    passed = sum(1 for result in results if result.passed)
    total = len(results)
    score = 0 if total == 0 else round((passed / total) * 100)

    lines.append("")
    lines.append(f"Score: {score}%")

    return "\n".join(lines)
