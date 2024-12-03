from pathlib import Path 
import re

file_path = Path(__file__).with_name("input.txt")
with file_path.open("r") as f:
    file_content = f.read()

# -----General----

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

number_pattern = r"[0-9]{1,3},[0-9]{1,3}"
  
# -----Code Part 1-----
pattern1_part1 = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

combination1 = find_pattern(file_content, pattern1_part1)
processed_combnination1 = process_pattern(combination1, number_pattern)
part1_result = multiply(processed_combnination1)

print(part1_result)

# -----Code Part 2-----
pattern1_part2 = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"

def clean_instructions(input):
  skip = False
  instructions = []
  
  for item in input:
    if item == "don't()":
      skip = True
    elif item == "do()":
      skip = False
    elif not skip:
      instructions.append(item)
      
  return instructions
  

combination2 = find_pattern(file_content, pattern1_part2)
clean_combinations = clean_instructions(combination2)
processed_combnination2 = process_pattern(clean_combinations, number_pattern)
part2_result = multiply(processed_combnination2)

print(part2_result)

# -----Documentation-----
