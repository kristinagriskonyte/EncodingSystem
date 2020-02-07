import webbrowser
def wiki(Cipher):
  if Cipher == 'C':
    print("Read about Caesar cipher to understand how it works")
    webbrowser.open('https://en.wikipedia.org/wiki/Caesar_cipher')
  if Cipher == 'At':
    print("Read about Atbash cipher to understand how it works")
    webbrowser.open('https://en.wikipedia.org/wiki/Atbash')
  if Cipher == 'Af':
    print("Read about Affine cipher to understand how it works")
    webbrowser.open('https://en.wikipedia.org/wiki/Affine_cipher')
  if Cipher == 'V':
    print("Read about Vigenere cipher to understand how it works")
    webbrowser.open('https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher')