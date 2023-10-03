print('import submoduleA')

from pathlib import Path
def printpath():
    print(Path(__file__).absolute())