'''
tools 直下の exe1.py を __main__ から実行できるか確認する。
'''
from argparse import ArgumentParser, _SubParsersAction

import _path_adding

def add_argument(parser:ArgumentParser):
    subparsers = parser.add_subparsers()
    add_exe1(subparsers)
    add_exe2(subparsers)
    add_exe3(subparsers)
    add_exe4(subparsers)
    return parser


def main(*args, **kwargs):
    parser = ArgumentParser()
    parser = add_argument(parser)
    if "handler" not in kwargs.keys():
        parser.print_help()
    else:
        handler = kwargs.pop("handler")
        handler(**kwargs)


def add_exe1(subpasers:_SubParsersAction):
    from dirtest.tools import exe1
    parser: ArgumentParser = subpasers.add_parser("exe1")
    parser = exe1.add_argument(parser)
    parser.set_defaults(handler=exe1.main)


def add_exe2(subpasers:_SubParsersAction):
    from dirtest.tools import exe2
    parser: ArgumentParser = subpasers.add_parser("exe2")
    parser = exe2.add_argument(parser)
    parser.set_defaults(handler=exe2.main)


def add_exe3(subpasers:_SubParsersAction):
    from dirtest.tools import exe3
    parser: ArgumentParser = subpasers.add_parser("exe3")
    parser = exe3.add_argument(parser)
    parser.set_defaults(handler=exe3.main)


def add_exe4(subpasers:_SubParsersAction):
    from dirtest.tools import exe4
    parser: ArgumentParser = subpasers.add_parser("exe4")
    parser = exe4.add_argument(parser)
    parser.set_defaults(handler=exe4.main)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser = add_argument(parser)
    main(**vars(parser.parse_args()))