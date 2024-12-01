from pathlib import Path
import itertools

file_path = Path(__file__).with_name("input.txt")

with file_path.open("r") as f:
    file_content = f.readlines() 

# -----Code Part 1-----
part1_content = [list(map(int, line.strip().split())) for line in file_content]

safety = [
    [int(a) - int(b) for a, b in itertools.pairwise(report)]
    for report in part1_content
]

filtered_safety = [
    sublist for sublist in safety
    if (all(x > 0 for x in sublist) or all(x < 0 for x in sublist)) 
    and all(1 <= abs(x) <= 3 for x in sublist)                     
]

print(len(filtered_safety))

# -----Code Part 2-----
#tbd - Not solved in time