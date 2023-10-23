from argparse import ArgumentParser, _SubParsersAction

import _path_adding


def add_argument(parser:ArgumentParser):
    subparsers = parser.add_subparsers()
    add_exe41(subparsers)
    add_exe42(subparsers)

    return parser


def main(*args, **kwargs):
    parser = ArgumentParser()
    parser = add_argument(parser)
    if "handler" not in kwargs:
        parser.print_help()
    else:
        handler = kwargs.pop("handler")
        handler(**kwargs)


def add_exe41(subpasers:_SubParsersAction):
    from dirtest.tools.exe4 import exe41
    parser: ArgumentParser = subpasers.add_parser("exe41")
    parser = exe41.add_argument(parser)
    parser.set_defaults(handler=exe41.main)


def add_exe42(subpasers:_SubParsersAction):
    from dirtest.tools.exe4 import exe42
    parser: ArgumentParser = subpasers.add_parser("exe42")
    parser = exe42.add_argument(parser)
    parser.set_defaults(handler=exe42.main)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser = add_argument(parser)
    main(**vars(parser.parse_args()))