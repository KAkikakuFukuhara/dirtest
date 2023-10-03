'''
シンボリックリンクでリンクされている pkgs/submodule_a を読み込む
'''

from argparse import ArgumentParser

import _path_adding
from dirtest.sa import modsa


def parse_args():
    parser = ArgumentParser(description=__doc__)
    return vars(parser.parse_args())


def main(*args, **kwargs):
    modsa.printpath()


if __name__ == "__main__":
    main(**parse_args())