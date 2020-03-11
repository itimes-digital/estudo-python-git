"""Escrevendo JSON"""
import json

pessoa = {}
pessoa["Nome"] = "Elvis Presley"
pessoa["Profissao"] = "Cantor"

filename = 'C:\\Users\\admin\\Documents\\estudos\\text-file\\numbers.json'

with open(filename, 'w') as f_obj:
	json.dump(pessoa, f_obj)


