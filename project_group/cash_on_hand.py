from pathlib import Path
import csv



def coh_function():
    fp_read = Path.cwd() / "project_group" / "csv_reports" / "Cash On Hand.csv"
    fp_write = Path.cwd() / "project_group" / "summary_report.txt"
    fp_write.touch()

    coh_amount = []
    coh_days = []

    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            coh_days.append(row)
            coh_amount.append(int(row[1]))
    deficit = True
    final_results = []
    for number in range(1, len(coh_amount)-1):
        first_day = (coh_amount[number-1])
        second_day = (coh_amount[number])
        coh_difference = second_day - first_day
        results = coh_days[number][0]
        if coh_difference < 0:
            deficit = False
            final_results.append(f"\n[CASH DEFICIT]:DAY {float(results)}, AMOUNT: USD {abs(coh_difference)}")

    if deficit:
        final_results.append(f"\nCASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    with fp_write.open(mode="a", encoding="UTF-8") as file:
        for item in final_results:
            file.write(f"{item}\n")
