from pathlib import Path
import csv

fp_read = Path.cwd() / "project_group" / "csv_reports" / "Overheads.csv"
fp_write = Path.cwd() / "project_group" / "summary_report.txt"
fp_write.touch()

def overheads_function():
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        highest_overhead = (header[0], 0)
        for row in reader:
            overhead_category = row[0]
            overhead_amount = float(row[1])
            if overhead_amount > highest_overhead[1]:
                highest_overhead = (overhead_category, overhead_amount)
        with fp_write.open(mode='w',encoding='UTF-8') as file:
           file.write(f"[HIGHEST OVERHEADS] {highest_overhead[0]}: {highest_overhead[1]}%")
    return highest_overhead

summary = overheads_function()



