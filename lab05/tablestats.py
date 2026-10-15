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

def total_minutes(rows):
    total = 0.0
    found = False

    for row in rows:
        if row.get("тип") == kind:
            found = True
            minutes_str = row.get("минуты", "")
            try:
                minutes_val = float(minutes_str.replace(',', '.'))
                total += minutes_val
            except (ValueError, TypeError):
                continue
    if not found:
        return 0.0

    return round(total, 1)

def to_csv(counts):
    lines = ["тип,количество"]
    for kind in sorted(counts.keys()):
        lines.append(f"{kind},{counts[kind]}")

    return "\n".join(lines) + "/n"
