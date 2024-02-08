def extract_route(requisicao):
    return requisicao.split()[1][1:]


def read_file(filepath):
    with open(filepath, 'rb') as file:
        return file.read()