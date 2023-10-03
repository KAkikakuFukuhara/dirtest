'''
親ディレクトリにあるモジュールを読み込むテスト
'''
from argparse import ArgumentParser
from pathlib import Path

if __name__ == "__main__":
    import _path_adding
from dirtest import mod_a

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("dir", type=str)
    return vars(parser.parse_args())


def main(*args, **kwargs):
    dir_ = Path(kwargs["dir"])
    print(dir_)


if __name__ == "__main__":
    main(**parse_args())