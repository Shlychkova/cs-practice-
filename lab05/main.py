from pathlib import Path
from tablestats import *


def main():
    path = input().strip()

    with open(path, encoding="utf-8") as table:
        rows = read_rows(table)

    counts = count_types(rows)

    print(len(rows))
    print(len(counts))
    print(total_minutes(rows, "ошибка"))

    path = Path(__file__).with_name("summary.csv")
    with open(path, "w", encoding="utf-8") as out:
        out.write(to_csv(counts))


if __name__ == "__main__":
    main()
