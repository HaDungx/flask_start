import json

def txt_to_json(file_path):
  with open(file_path, "r",encoding = 'utf-8') as f:
    lines = f.readlines()

  dict = {}
  for line in lines:
    key = line
    key = key.strip()
    value = key
    dict[key] = value

  return dict