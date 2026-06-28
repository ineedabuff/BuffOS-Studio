from __future__ import annotations

import argparse
from pathlib import Path

from app.cli.apply.buff import run as apply_buff
from app.cli.apply.gaming import run as apply_gaming
from app.cli.apply.nvidia import run as apply_nvidia
from app.cli.apply.terminal import run as apply_terminal
from app.cli.doctor import run_doctor
from app.cli.modules import create_runner
from app.cli.setup.run import run as setup_run
from app.generators.terminal.generator import (
    generate_bash,
    generate_zsh,
)
from app.identity import APP_CLI, APP_NAME, VERSION


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=APP_CLI)

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("version", help="Show version")
    sub.add_parser("analyze", help="Analyze only")
    sub.add_parser("setup", help="Configure this computer")

    apply = sub.add_parser("apply", help="Apply profile")
    apply.add_argument(
        "target",
        nargs="?",
        default=None,
        choices=[
            "buff",
            "gaming",
            "nvidia",
            "terminal",
        ],
    )

    doctor = sub.add_parser("doctor", help="Run doctor")
    doctor.add_argument("--json", action="store_true")

    generate = sub.add_parser("generate", help="Generate files")
    generate.add_argument("target", choices=["terminal"])

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    match args.command:
        case "version":
            print(APP_NAME)
            print(f"Version {VERSION}")

        case "analyze":
            create_runner(dry_run=True).execute()

        case "setup":
            setup_run()

        case "doctor":
            run_doctor(json_output=args.json)

        case "apply":
            match args.target:
                case "buff":
                    apply_buff()
                case "gaming":
                    apply_gaming()
                case "nvidia":
                    apply_nvidia()
                case "terminal":
                    apply_terminal()
                case _:
                    create_runner().execute()

        case "generate":
            generate_bash(Path.home() / ".bashrc")
            generate_zsh(Path.home() / ".zshrc")
            print("✓ Buff terminal generated")

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
