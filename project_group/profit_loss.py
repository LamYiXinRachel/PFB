from pathlib import Path
import csv

def pnl_function():
    fp_read = Path.cwd() / "project_group" / "csv_reports" / "Profit and Loss.csv"
    fp_write = Path.cwd() / "project_group" / "summary_report.txt"

    pnl_list = []

    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            pnl_list.append((int(row[0]), float(row[1])))

    deficit = True
    final_results = []
    for number in range(1, len(pnl_list)):
        first_day = pnl_list[number-1][1]
        second_day = pnl_list[number][1]
        pnl_difference = second_day - first_day
        if pnl_difference < 0:
            deficit = False
            final_results.append(f"[PROFIT DEFICIT]:DAY {(pnl_list[number][0])}, AMOUNT: USD {-(pnl_difference)}")

    if deficit:
        final_results.append(f"NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    with fp_write.open(mode="a", encoding="UTF-8") as file:
        for item in final_results:
            file.write(f"{item}\n")
            file.close()
