from app.cli.main import build_parser


def test_program_name():
    parser = build_parser()
    assert parser.prog == "buff"
