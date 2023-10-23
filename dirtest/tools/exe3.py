'''
/pkgs/submodb/pkgs/sba を読み込む
'''
from argparse import ArgumentParser

if __name__ == "__main__":
    import _path_adding

from dirtest.sb import modsb
from dirtest.sb.sba import modsba


def add_argument(parser:ArgumentParser) -> ArgumentParser:
    return parser


def main(*args, **kwargs):
    modsb.print_path()
    modsba.print_path()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser = add_argument(parser)
    main(**vars(parser.parse_args()))    


