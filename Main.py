import webbrowser
import os
from classAffine import *
from classAtbash import *
from classCaessar import *
from VigenereCipher import *
from Wiki import *
from Results import *

os.chdir("EncodingSystem")
alphabetDirectory = 'Alphabets/'
all_files = os.listdir(alphabetDirectory)

inputCipher = []
inputCipher = input("Type 'C' to use Casear cipher, 'At' to use Atbash cipher, 'Af' to use Affine cipher or 'V' to use Vigenere cipher: ")
while inputCipher!='C' and inputCipher!='At' and inputCipher!='Af' and inputCipher!='V':
    inputCipher = input("You have selected unknown command. Please, type 'C' to use Casear cipher, 'At' to use Atbash cipher, 'Af' to use Affine cipher or 'V' to use Vigenere cipher: ")

wiki(inputCipher)

inputEncodeDecode = []
inputEncodeDecode = input("Type 'E' to encrypt, 'D' to decrypt: ")
while inputEncodeDecode!='E' and inputEncodeDecode!='D' and inputEncodeDecode!='B':
    inputEncodeDecode = input("You have selected unknown command. Please, type 'E' to encrypt or 'D' to decrypt: ")

inputTextType = []
inputTextType = input("Type 'S' to select text from file or 'C' to type text in command line: ")
while inputTextType != 'S' and inputTextType != 'C':
    inputTextType = input("You have selected unknown command. Please, type 'S' to select text from file or 'C' to type text in command line: ")
if inputTextType == 'S':
    inputFile = input("Type the file name with directory: ")
    inputText = list(open(inputFile,"r", encoding = "utf8").read().lower())
else:
    inputText = list(input("Input to encrypt or decrypt: ").lower())

inputAlphabet=[]
inputAlphabet = input("Do you have your own alphabet? 'Y' - yes, 'N' - No: " )
while inputAlphabet != 'Y' and inputAlphabet != 'N':
    inputAlphabet=input("You have selected unknown command. Please, type 'Y' if you want to use your alphabet or 'N' to select from existing alphabets: ")
if inputAlphabet == 'Y':
    inputAlphabetPath = input("Please, type alphabet file name with directory: ")
    inputAlphabet = open(inputAlphabetPath, "r", encoding = "utf8").read()
else:
    print("See the list of alphabets: ")
    print(*all_files, sep='\n')
    inputAlphabetChosen = input("Which alphabet you want to use: " )
    inputAlphabet = open(alphabetDirectory + inputAlphabetChosen, "r", encoding = "utf8").read()

if inputCipher == 'C':
    encodingKey = []
    print("Encoding key should not be longer than: " + str(len(inputAlphabet)))
    encodingKey = int(input("What is your encoding key: " ))
    while encodingKey>len(inputAlphabet):
        print("Encoding key should not be longer than: " + str(len(inputAlphabet)))
        encodingKey = int(input("What is your encoding key: " ))

if inputCipher == 'Af':
    encodingKey1 = []
    encodingKey2 = []
    print("Encoding key1 should not be longer than: " + str(len(inputAlphabet)))
    encodingKey1 = int(input("What is your encoding key1: " ))
    while encodingKey1>len(inputAlphabet):
        print("Encoding key1 should not be longer than: " + str(len(inputAlphabet)))
        encodingKey1 = int(input("What is your encoding key1: " ))
    print("Encoding key2 should not be longer than: " + str(len(inputAlphabet)))
    encodingKey2 = int(input("What is your encoding key2: " ))
    while encodingKey2>len(inputAlphabet):
        print("Encoding key2 should not be longer than: " + str(len(inputAlphabet)))
        encodingKey2 = int(input("What is your encoding key2: " ))

if inputCipher == 'V':
    encodingKeyword = str(input("Please type your encoding keyword: " ))
    print(encodingKeyword)

if inputCipher == 'V':
  alphabet = {k:v for k,v in enumerate(inputAlphabet)}

if inputCipher == 'C':
    Message = Caessar(inputText, encodingKey, inputAlphabet)
    if inputEncodeDecode == 'E':
        result = Message.encode()
    elif inputEncodeDecode == 'D':
        result = Message.decode()

if inputCipher == 'Af':
    Message = Affine(inputText, encodingKey1, encodingKey2, inputAlphabet)
    if inputEncodeDecode == 'E':
        result = Message.encode()
    elif inputEncodeDecode == 'D':
        result = Message.decode()

if inputCipher == 'At':
    Message = Atbash(inputText, inputAlphabet)
    if inputEncodeDecode == 'E':
        result = Message.encode()
    elif inputEncodeDecode == 'D':
        result = Message.decode()

if inputCipher == 'V':
    vigenereKey = generateKey(inputText, encodingKeyword).lower()
    print(vigenereKey)
    alphabet = {k:v for k,v in enumerate(inputAlphabet)}
    if inputEncodeDecode == 'E':
         result = encodeVigenere(inputText, alphabet, vigenereKey)
    else:
        result = decodeVigenere(inputText, alphabet, vigenereKey)

results(inputText, inputEncodeDecode, inputCipher, result)