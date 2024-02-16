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
    
def adiciona_note(note):  
    y = Path("data")/"notes,json"
    if y.exists():
        with open(y, 'r') as file:
            data = json.load(file)
    else:
        data = []
    data.append(note)   
    with open(y, 'w') as file:
        json.dump(data, file) 

def build_response(body="", code=200, reason="ok", headers=""):
    if headers == "":
        string = f"HTTP/1.1 {code} {reason}\n\n{body}"
    else:
        string = f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}"
    return string.encode()

