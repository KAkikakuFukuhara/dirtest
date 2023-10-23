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
    if not __name__ == "__main__":
        parser.print_help()
    elif "handler" not in kwargs:
        parser.print_help()
    else:
        kwargs["handler"](**kwargs)


def add_exe41(subpasers:_SubParsersAction):
    from dirtest.tools.exe4 import exe41
    parser: ArgumentParser = subpasers.add_parser("exe41")
    parser = exe41.add_argument(parser)

    def callback(*args, **kwargs):
        exe41.main(**kwargs)

    parser.set_defaults(handler=callback)


def add_exe42(subpasers:_SubParsersAction):
    from dirtest.tools.exe4 import exe42
    parser: ArgumentParser = subpasers.add_parser("exe42")
    parser = exe42.add_argument(parser)

    def callback(*args, **kwargs):
        exe42.main(**kwargs)

    parser.set_defaults(handler=callback)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser = add_argument(parser)
    main(**vars(parser.parse_args()))