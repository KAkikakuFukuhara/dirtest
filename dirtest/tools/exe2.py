'''
シンボリックリンクでリンクされている pkgs/submodule_a を読み込む
'''

from argparse import ArgumentParser

import _path_adding
from dirtest.submodule_a import submodule_a


def parse_args():
    parser = ArgumentParser(description=__doc__)
    return vars(parser.parse_args())


def main(*args, **kwargs):
    submodule_a.printpath()


if __name__ == "__main__":
    main(**parse_args())