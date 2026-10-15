def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        values = line.split(",")
        for i in range(len(values)):
            values[i] = values[i].strip()
def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        values = line.split(",")
        for i in range(len(values)):
            values[i] = values[i].strip()

        if not header:
            header = values
            continue

        if len(values) != len(header):
            continue

        row = {}
        for i in range(len(header)):
            row[header[i]] = values[i]
        rows.append(row)

    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}

    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1

    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0

    for row in rows:
        if row["тип"] != kind:
            continue

        try:
            total += float(row["минуты"].replace(",", "."))
        except ValueError:
            continue

    return round(total, 1)


def to_csv(counts: dict) -> str:
    result = "тип,количество\n"

    for kind in sorted(counts):
        result += f"{kind},{counts[kind]}\n"

    return result
        if not header:
            header = values
            continue

        if len(values) != len(header):
            continue

        row = {}
        for i in range(len(header)):
            row[header[i]] = values[i]
        rows.append(row)

    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}

    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1

    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0

    for row in rows:
        if row["тип"] != kind:
            continue

        try:
            total += float(row["минуты"].replace(",", "."))
        except ValueError:
            continue

    return round(total, 1)


def to_csv(counts: dict) -> str:
    result = "тип,количество\n"

    for kind in sorted(counts):
        result += f"{kind},{counts[kind]}\n"

    return result
