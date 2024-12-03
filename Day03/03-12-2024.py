from pathlib import Path 
import re

file_path = Path(__file__).with_name("input.txt")
with file_path.open("r") as f:
    file_content = f.read()
    
# -----Code Part 1-----
def find_pattern(input):
    pattern1 = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)", re.IGNORECASE)
    pattern2 = re.compile(r"[0-9]{1,3},[0-9]{1,3}", re.IGNORECASE)
    new_content = pattern1.findall(input)
    numbers = [pattern2.findall(item)[0].split(",") for item in new_content]
    numbers = [[int(item[0]), int(item[1])] for item in numbers]
    return numbers
  
combination = find_pattern(file_content)

sum=0
for item in combination:
  sum += (item[0]*item[1])

print(sum)



# -----Code Part 2-----



# -----Documentation-----
