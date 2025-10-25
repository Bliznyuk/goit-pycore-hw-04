import sys
import pathlib
import colorama

colorama.init(autoreset=True)

try:
    path: str = sys.argv[1]
except IndexError:
    print(f"{colorama.Fore.RED}Please provide a path to a directory.")
    sys.exit(1)

path_obj = pathlib.Path(path)
if not path_obj.exists():
    print(f"{colorama.Fore.RED}The path {path} doesn't exist.")
    sys.exit(1)

if not path_obj.is_dir():
    print(f"{colorama.Fore.RED}The path {path} is not a directory.")
    sys.exit(1)

CONNECTOR_L = "┗"
CONNECTOR_T = "┣"
CONNECTOR_I = "┃"
CONNECTOR_EMPTY = " "


def print_tree(dirpath: pathlib.Path, prefix: str = ""):
    """
    Recursively prints the directory tree structure starting from dirpath.

    E.g.:
    ```
    📦 root
     ┣ 📂 subdir1
     ┃  ┣ 📜 file1.txt
     ┃  ┗ 📜 file2.txt
     ┗ 📂 subdir2
        ┗ 📜 file3.txt
    ```
    """
    dir_contents = list(dirpath.iterdir())
    dir_contents_couunt = len(dir_contents)
    for index, item in enumerate(dir_contents):
        is_last = dir_contents_couunt == index + 1
        current_connector = CONNECTOR_L if is_last else CONNECTOR_T

        if item.is_dir():
            print(f"{prefix} {current_connector} 📂 {colorama.Fore.BLUE}{item.name}")
            next_level_connector = CONNECTOR_EMPTY if is_last else CONNECTOR_I
            print_tree(item, f"{prefix} {next_level_connector} ")
        else:
            print(f"{prefix} {current_connector} 📜 {colorama.Fore.GREEN}{item.name}")


print(f"📦 {colorama.Fore.RED}{path_obj.name}")
print_tree(path_obj)
