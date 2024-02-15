import json
from pathlib import Path

def extract_route(requisicao):
    return requisicao.split()[1][1:]

def read_file(filepath):
    with open(filepath, 'rb') as file:
        return file.read()
    
def load_data(arquivo):
    x = Path("data")/arquivo
    with open(x, 'r') as file:
        return json.load(file)
    

def load_template(nome):
    with open(f"templates/{nome}", 'r') as file:
        return file.read()
    
