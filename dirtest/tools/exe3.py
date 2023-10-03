'''
/pkgs/submodb/pkgs/sba を読み込む
'''
from argparse import ArgumentParser

if __name__ == "__main__":
    import _path_adding

from dirtest.sb import modsb
from dirtest.sb.sba import modsba


def parse_args():
    parser = ArgumentParser(description=__doc__)
    return vars(parser.parse_args())


def main(*args, **kwargs):
    modsb.print_path()
    modsba.print_path()


if __name__ == "__main__":
    main(**parse_args())


