from app.cli.main import build_parser


def test_cli_commands():
    parser = build_parser()

    assert parser.parse_args(["analyze"]).command == "analyze"
    assert parser.parse_args(["apply"]).command == "apply"
    assert parser.parse_args(["version"]).command == "version"
