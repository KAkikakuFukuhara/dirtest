'''
tools 直下の exe1.py を __main__ から実行できるか確認する。
'''
from argparse import ArgumentParser, _SubParsersAction

import _path_adding

def parse_args():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()
    add_exe1(subparsers)
    add_exe2(subparsers)
    add_exe3(subparsers)
    add_exe4(subparsers)

    cli_kwargs = vars(parser.parse_args())
    if "handler" not in cli_kwargs.keys():
        parser.print_help()
    return cli_kwargs


def main(*args, **kwargs):
    if "handler" in kwargs.keys():
        kwargs["handler"](**kwargs)


def add_exe1(subpasers:_SubParsersAction):
    from dirtest.tools import exe1
    parser: ArgumentParser = subpasers.add_parser("exe1")
    parser = exe1.add_argument(parser)

    def callback(*args, **kwargs):
        exe1.main(**kwargs)

    parser.set_defaults(handler=callback)


def add_exe2(subpasers:_SubParsersAction):
    from dirtest.tools import exe2
    parser: ArgumentParser = subpasers.add_parser("exe2")
    parser = exe2.add_argument(parser)

    def callback(*args, **kwargs):
        exe2.main(**kwargs)

    parser.set_defaults(handler=callback)


def add_exe3(subpasers:_SubParsersAction):
    from dirtest.tools import exe3
    parser: ArgumentParser = subpasers.add_parser("exe3")
    parser = exe3.add_argument(parser)

    def callback(*args, **kwargs):
        exe3.main(**kwargs)

    parser.set_defaults(handler=callback)


def add_exe4(subpasers:_SubParsersAction):
    from dirtest.tools import exe4
    parser: ArgumentParser = subpasers.add_parser("exe4")
    parser = exe4.add_argument(parser)

    def callback(*args, **kwargs):
        exe4.main(**kwargs)

    parser.set_defaults(handler=callback)


if __name__ == "__main__":
    main(**parse_args())