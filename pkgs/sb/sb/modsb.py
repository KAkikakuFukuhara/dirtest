from pathlib import Path
def print_path():
    print(Path(__file__).absolute())

print("import ", end="")
print_path()
