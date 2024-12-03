from pathlib import Path 
import re

file_path = Path(__file__).with_name("test.txt")
with file_path.open("r") as f:
    file_content = f.read()
    
def multiply(input):
  sum = 0
  for item in input:
    sum += (item[0]*item[1])
  return sum
  
def find_pattern(input, p1):
    pattern1 = re.compile(p1, re.IGNORECASE)
    new_content = pattern1.findall(input)
    return new_content
  
def process_pattern(input, p2):
  pattern2 = re.compile(p2, re.IGNORECASE)
  numbers = [pattern2.findall(item)[0].split(",") for item in input]
  numbers = [[int(item[0]), int(item[1])] for item in numbers]
  return numbers
  
  
# -----Code Part 1-----
pattern1_part1 = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
pattern2_part1 = r"[0-9]{1,3},[0-9]{1,3}"

combination = find_pattern(file_content, pattern1_part1)
processed_combnination = process_pattern(combination, pattern2_part1)
part1_result = multiply(processed_combnination)

print(part1_result)

# -----Code Part 2-----


# -----Documentation-----
