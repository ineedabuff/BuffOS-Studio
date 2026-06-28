from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


def ok_fn(text: str) -> None:
    print(f"\033[92m✓\033[0m {text}")


def fail(text: str) -> None:
    print(f"\033[91m✗\033[0m {text}")


def print_check(label: str, ok: bool) -> None:
    print(f"{'✓' if ok else '✗'} {label}")


def check(label: str, value: bool) -> bool:
    (ok_fn if value else fail)(label)
    return value


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def systemd(unit: str) -> bool:
    return (
        subprocess.run(
            ["systemctl", "is-active", "--quiet", unit],
            check=False,
        ).returncode
        == 0
    )


def flatpak(app: str) -> bool:
    return (
        subprocess.run(
            ["flatpak", "info", app],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def build_report() -> dict:
    storage = {
        "Timeshift": command_exists("timeshift"),
        "grub-btrfs": systemd("grub-btrfsd.service"),
        "fstrim": systemd("fstrim.timer"),
        "Scrub": systemd("btrfs-scrub.timer"),
    }

    gaming = {
        "NVIDIA": command_exists("nvidia-smi"),
        "Steam": command_exists("steam"),
        "GameMode": command_exists("gamemoded"),
        "MangoHud": command_exists("mangohud"),
        "PortProton": flatpak("ru.linux_gaming.PortProton"),
    }

    checks = list(storage.values()) + list(gaming.values())

    return {
        "storage": storage,
        "gaming": gaming,
        "score": round(sum(checks) / len(checks) * 100),
    }


def write_html(report: dict) -> Path:
    html = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Buff Helper Doctor</title>
<style>
body{{background:#000;color:#fff;font-family:Inter,Arial;padding:40px}}
h1{{color:#ddff24}}
h2{{color:#1F51FF}}
.ok{{color:#0FFF50}}
.bad{{color:#ff3131}}
.score{{font-size:32px;color:#ddff24;font-weight:bold}}
</style>
</head>
<body>

<h1>Buff Helper Doctor</h1>

<div class="score">
BUFF READY : {report["score"]}%
</div>

<h2>Storage</h2>
<ul>
{''.join(f'<li class="{"ok" if v else "bad"}">{k}</li>' for k,v in report["storage"].items())}
</ul>

<h2>Gaming</h2>
<ul>
{''.join(f'<li class="{"ok" if v else "bad"}">{k}</li>' for k,v in report["gaming"].items())}
</ul>

</body>
</html>
"""

    out = Path.home() / "buff-helper-report.html"
    out.write_text(html, encoding="utf-8")
    return out


def run_doctor(*, json_output: bool = False) -> None:
    report = build_report()

    if json_output:
        print(json.dumps(report, indent=2))
        return

    print()
    print("\033[1;97mBuff Helper Doctor\033[0m")
    print("=" * 40)

    print("\n\033[96mStorage\033[0m")
    for k, v in report["storage"].items():
        check(k, v)

    print("\n\033[96mGaming\033[0m")
    for k, v in report["gaming"].items():
        check(k, v)

    print("\n" + "=" * 40)
    print(f"BUFF READY : {report['score']}%")

    html = write_html(report)
    print(f"\nHTML Report : {html}")
