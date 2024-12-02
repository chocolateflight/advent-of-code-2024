from pathlib import Path

file_path = Path(__file__).with_name("input.txt")

with file_path.open("r") as f:
  file_content = f.read()
  
  