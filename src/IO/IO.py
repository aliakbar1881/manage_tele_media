from pathlib import Path
import json


from src.inputfile import INPUTFILE

def read_text_file(txt):
    txt = INPUTFILE / txt
    with open(txt, 'rb') as open_txt:
        entity = open_txt.read()
    return entity

def read_json(json_file):
    json_file = Path(INPUTFILE) / json_file
    with open(json_file) as json_file:
        content = json.load(json_file)
    return content


if __name__ == '__main__':
    test = INPUTFILE / 'test.txt'
    print(read_text_file(test))

