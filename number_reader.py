"""Lendo JSON"""
import json

filename = 'C:\\Users\\admin\\Documents\\estudos\\text-file\\numbers.json'

with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)
