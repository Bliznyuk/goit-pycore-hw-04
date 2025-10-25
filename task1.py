import pathlib


def total_salary(path: str) -> tuple[int, int]:
    """
    Reads a file containing employee salaries and returns the total and average salary.
    """
    # If file does not exist, raise FileNotFoundError
    if not pathlib.Path(path).exists():
        raise FileNotFoundError(f"The file at {path} does not exist.")

    # Knowing that file exists, we can proceed to open and read it
    with open(path, "r", encoding="utf-8") as salary_file:
        all_lines = salary_file.readlines()

        total_sum = 0

        for line in all_lines:
            try:
                # eg. Alex Korp,3000 parse line to get only salary
                _, salary = line.split(",")
            except ValueError:
                raise ValueError(
                    f"Line '{line.strip()}' is not in the expected 'Name,Salary' format."
                )
            # We use strip to get rid of /n at the end of the salary string
            total_sum += int(salary.strip())

        return (total_sum, int(total_sum / len(all_lines)))


total, average = total_salary("files/salary_file.txt")
print(f"Total salary {total}, Average salary {average}")
