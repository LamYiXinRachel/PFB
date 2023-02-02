# import all 3 modules
import cash_on_hand, profit_loss, overheads

def main():
    """
    - This function will find the highest overheads category and put it in percentage 
    - This function will compute the difference in Cash-on-Hand if 
    the current day is lower than the previous day
    - This function will compute the difference in the net profit column if
    net profit on the current day is lower than the previous day
    """

    overheads.overheads_function()
    cash_on_hand.coh_function()
    profit_loss.pnl_function()

main()

# import Path method from pathlib
from pathlib import Path

# create a file path pointing to the current working directory to store group members' details
group_path = Path.cwd() / "project_group" / "team_members.txt"

# creates a new file in the file path with .touch()
group_path.touch()

# open file using 'with' and 'open' keyword in 'write' mode
with group_path.open(mode = "w", encoding="UTF-8") as file:
    file.write("Choo Tze An Ryan (S10220901F)\nChow Jun Ci, Emily (S10241912A)\nLam Yi Xin Rachel (S10220993A)\nTer Xin Yi (S10204687C)")
