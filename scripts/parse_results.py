import re
import csv
from pathlib import Path

CPU_RE  = re.compile(r"CPU time\s*:\s*([\d.]+)\s*s")
MEM_RE  = re.compile(r"Memory used\s*:\s*([\d.]+)\s*MB")
CONF_RE = re.compile(r"conflicts\s*:\s*(\d+)")
DEC_RE  = re.compile(r"decisions\s*:\s*(\d+)")
PROP_RE = re.compile(r"propagations\s*:\s*(\d+)")

FIELDS = [
    "instance","os","status","cpu_time_s",
    "conflicts","decisions","propagations","memory_mb"
]

def parse_file(path: Path):
    text = path.read_text(errors="ignore")

    def find(regex):
        m = regex.search(text)
        return m.group(1) if m else ""

    status = "UNKNOWN"
    if "UNSATISFIABLE" in text:
        status = "UNSATISFIABLE"
    elif "SATISFIABLE" in text:
        status = "SATISFIABLE"

    return {
        "cpu_time_s": find(CPU_RE),
        "memory_mb": find(MEM_RE),
        "conflicts": find(CONF_RE),
        "decisions": find(DEC_RE),
        "propagations": find(PROP_RE),
        "status": status,
    }

def to_number(s):
    if s is None or s == "":
        return None
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        return s

def main():
    raw_dir = Path("results/raw")
    if not raw_dir.exists():
        raise SystemExit("Missing results/raw folder. Put your *.txt logs in results/raw/")

    rows = []
    for path in sorted(raw_dir.glob("*.txt")):
        stem = path.stem.lower()

        if "windows" in stem:
            os_name = "windows"
        elif "macos" in stem or "osx" in stem:
            os_name = "macos"
        else:
            os_name = "unknown"

        base = stem
        for suffix in ["_windows", "_macos", "_osx"]:
            base = base.replace(suffix, "")

        instance = base + ".cnf"

        data = parse_file(path)
        row = {"instance": instance, "os": os_name, **data}

        for k in ["cpu_time_s","memory_mb","conflicts","decisions","propagations"]:
            row[k] = to_number(row.get(k, ""))

        rows.append(row)

    out_csv = Path("results/results.csv")
    out_xlsx = Path("results/results.xlsx")

    with out_csv.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)

    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, Alignment
    except ImportError:
        print("openpyxl not installed. Generated CSV only:", out_csv)
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "results"

    ws.append(FIELDS)
    header_font = Font(bold=True)
    for col_idx, name in enumerate(FIELDS, start=1):
        cell = ws.cell(row=1, column=col_idx, value=name)
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center")

    for r in rows:
        ws.append([r.get(k, None) for k in FIELDS])

    ws.freeze_panes = "A2"

    for row in ws.iter_rows(min_row=2):
        if row[3].value is not None:
            row[3].number_format = "0.00"
        if row[7].value is not None:
            row[7].number_format = "0.00"

    for col_idx, col_name in enumerate(FIELDS, start=1):
        max_len = len(col_name)
        for cell in ws.iter_rows(min_row=2, min_col=col_idx, max_col=col_idx, values_only=True):
            v = cell[0]
            if v is None:
                continue
            max_len = max(max_len, len(str(v)))
        ws.column_dimensions[chr(64 + col_idx)].width = min(max_len + 2, 60)

    wb.save(out_xlsx)
    print("Generated:", out_csv, "and", out_xlsx)

if __name__ == "__main__":
    main()