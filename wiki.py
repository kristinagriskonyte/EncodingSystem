import webbrowser
def open_wiki(cipher):
    if cipher == 'C':
        print("Read about Caesar cipher to understand how it works")
        webbrowser.open('https://en.wikipedia.org/wiki/Caesar_cipher')
    if cipher == 'At':
        print("Read about Atbash cipher to understand how it works")
        webbrowser.open('https://en.wikipedia.org/wiki/Atbash')
    if cipher == 'Af':
        print("Read about Affine cipher to understand how it works")
        webbrowser.open('https://en.wikipedia.org/wiki/Affine_cipher')
    if cipher == 'V':
        print("Read about Vigenere cipher to understand how it works")
        webbrowser.open('https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher')
