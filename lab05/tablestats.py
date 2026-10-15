def read_rows(lines):
    rows = []
    header = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = [part.strip() for part in line.split(',')]
        if not header:
            header = parts
            continue
        if len(parts) != len(header):
            continue
        row_dict = {}
        for i in range(len(header)):
            row_dict[header[i]] = parts[i]

        rows.append(row_dict)

    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
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
