from __future__ import annotations

import argparse

from app.core.runner import Runner


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="buffos")

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("analyze", help="Analyze the system")
    sub.add_parser("apply", help="Analyze and repair the system")
    sub.add_parser("version", help="Show BuffOS Studio version")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    match args.command:
        case "version":
            print("BuffOS Studio")

        case "analyze":
            Runner(dry_run=True).execute()

        case "apply":
            Runner().execute()

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
