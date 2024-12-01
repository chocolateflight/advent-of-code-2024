from pathlib import Path

# Variables
file_path = Path(__file__).with_name("input.txt")
file_content = ""
list1 = []
list2 = []
difference = 0

# Code Part 1

with file_path.open("r") as f:
  file_content = f.read().split()

for i in range(len(file_content)):
  if i%2 == 0:
    list1.append(file_content[i])
  else:
    list2.append(file_content[i])

list1.sort()
list2.sort()

for i in range(len(list1)):
  dif = abs(int(list1[i])-int(list2[i]))
  difference += dif
  
print(difference)