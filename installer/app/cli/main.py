from __future__ import annotations

import argparse


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

    if args.command == "version":
        print("BuffOS Studio")
        return

    if args.command == "analyze":
        print("Analyze mode")
        return

    if args.command == "apply":
        print("Apply mode")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
