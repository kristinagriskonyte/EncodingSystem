import webbrowser
def directory_establishment(cipher):
    switcher = {
        'C':'caessar/',
        'At':'atbash/',
        'Af':'affine/',
        'V': 'vigenere/'
    }
    return switcher.get(cipher)

def open_wiki(cipher):
    directory=directory_establishment(cipher)
    print("Read about your selected cipher")
    webbrowser.open(open(directory + "wiki.txt", "r", encoding = "utf8").read())


