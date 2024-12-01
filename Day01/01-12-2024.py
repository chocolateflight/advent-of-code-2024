from pathlib import Path

# Variables
file_path = Path(__file__).with_name("test.txt")
file_content = ""
list1 = []
list2 = []

# Code Part 1

with file_path.open("r") as f:
  file_content = f.read().split()

for i in range(len(file_content)):
  if i%2 == 0:
    list1.append(file_content[i])
  else:
    list2.append(file_content[i])

list1_part1 = sorted(list1)
list2_part1 = sorted(list2)

solution_part1 = 0

for i in range(len(list1_part1)):
  dif = abs(int(list1_part1[i])-int(list2_part1[i]))
  solution_part1 += dif
  
print(solution_part1)

