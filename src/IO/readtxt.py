from pathlib import Path


from  src.inputfile import INPUTFILE

def read_text_file(txt):
    txt = INPUTFILE / txt
    with open(txt, 'rb') as open_txt:
        entity = open_txt.read()
    return entity


if __name__ == '__main__':
    test = INPUTFILE / 'test.txt'
    print(read_text_file(test))

