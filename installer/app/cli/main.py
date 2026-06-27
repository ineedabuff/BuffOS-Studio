from __future__ import annotations

import argparse

from app.cli.modules import create_runner
from app.identity import APP_CLI, APP_NAME, VERSION


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=APP_CLI)

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("version", help="Show version")
    sub.add_parser("analyze", help="Analyze only")
    sub.add_parser("apply", help="Analyze and repair")

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

        case "apply":
            create_runner().execute()

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
