import pathlib


def get_cats_info(path: str) -> list[dict]:
    """
    Reads a file containing cat information and returns a list of dictionaries with cat details.
    """
    # If file does not exist, raise FileNotFoundError
    if not pathlib.Path(path).exists():
        raise FileNotFoundError(f"The file at {path} does not exist.")

    with open(path, "r", encoding="utf-8") as cats_file:
        all_lines = cats_file.readlines()
        cats = []

        for line in all_lines:
            try:
                # We remove \n characters and split the line by comma to get cat info into separate variables
                cat_id, name, age = line.strip().split(",")
                cats.append({"id": cat_id, "name": name, "age": age})

            except ValueError:
                raise ValueError(f"Wrong line format in cats file: {line.strip()}")

    return cats


cats_info = get_cats_info("files/cats_file.txt")
print(cats_info)
