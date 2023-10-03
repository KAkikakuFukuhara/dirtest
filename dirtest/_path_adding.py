import sys
from pathlib import Path

def _add_proj_path():
    file_dir: Path = Path(__file__).absolute().parent
    proj_dir: Path = file_dir.parent
    if str(proj_dir) not in sys.path:
        sys.path.insert(0, str(proj_dir))

_add_proj_path()