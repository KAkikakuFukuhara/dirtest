'''
tools 直下の exe1.py を __main__ から実行できるか確認する。
'''
from argparse import ArgumentParser, _SubParsersAction

import _path_adding

def parse_args():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()
    add_exe1(subparsers)

    cli_kwargs = vars(parser.parse_args())
    if "handler" not in cli_kwargs.keys():
        parser.print_help()
    return cli_kwargs


def main(*args, **kwargs):
    if "handler" in kwargs.keys():
        kwargs["handler"](**kwargs)


def add_exe1(subpasers:_SubParsersAction):
    parser: ArgumentParser = subpasers.add_parser("exe1")
    parser.add_argument("dir", type=str)

    def callback(*args, **kwargs):
        from dirtest.tools import exe1
        exe1.main(**kwargs)

    parser.set_defaults(handler=callback)


if __name__ == "__main__":
    main(**parse_args())