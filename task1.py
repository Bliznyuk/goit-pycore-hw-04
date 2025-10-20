import pathlib


def total_salary(path: str) -> tuple [int, int]:
    # 1 If file does not exist, raise FileNotFoundError
    if not pathlib.Path(path).exists():
        raise FileNotFoundError(f"The file at {path} does not exist.")

    # 2 Knowing that file exists, we can proceed to open and read it
    with open(path, "r", encoding="utf-8") as salary_file:
        all_lines = salary_file.readlines()

        total_sum = 0

        for line in all_lines:
            try:
                name, salary = line.split(",") # Alex Korp,3000
            except ValueError:
                raise ValueError(f"Line '{line.strip()}' is not in the expected 'Name,Salary' format.")
            total_sum += int(salary.strip())
        print(total_sum)

        return (total_sum, int(total_sum / len(all_lines)))



total_salary("files/salary_file.txt")

