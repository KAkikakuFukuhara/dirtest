'''
シンボリックリンクでリンクされている pkgs/submodule_a を読み込む
'''

from argparse import ArgumentParser

import _path_adding
from dirtest.sa import modsa

def add_argument(parser:ArgumentParser) -> ArgumentParser:
    return parser


def main(*args, **kwargs):
    modsa.printpath()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser = add_argument(parser)
    main(**vars(parser.parse_args()))