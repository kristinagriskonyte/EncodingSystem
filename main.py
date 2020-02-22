import webbrowser
import os
import affine
import atbash
import caessar
import vigenere
import wiki
import results
import cipher_directory
import ast

os.chdir("EncodingSystem")
alphabet_directory = 'alphabets/'
all_files = os.listdir(alphabet_directory)

constants = ast.literal_eval(open("constants.txt", "r", encoding = "utf8").read())

input_cipher = []
while input_cipher!='C' and input_cipher!='At' and input_cipher!='Af' and input_cipher!='V':
    input_cipher = input(constants['cipher'])

directory=cipher_directory.cipher_directory(input_cipher)
wiki.open_wiki(directory)

input_encode_decode = []
while input_encode_decode!='E' and input_encode_decode!='D':
    input_encode_decode = input(constants['encode_decode'])

input_text_type = []
while input_text_type != 'S' and input_text_type != 'C':
    input_text_type = input(constants['text_type'])
if input_text_type == 'S':
    input_file = input(constants['directory'])
    input_text = list(open(input_file,"r", encoding = "utf8").read().lower())
else:
    input_text = list(input(constants['text']).lower())

input_alphabet=[]
while input_alphabet != 'Y' and input_alphabet != 'N':
    input_alphabet=input(constants['alphabet'])
if input_alphabet == 'Y':
    input_alphabet_path = input(constants['alphabet_file'])
    input_alphabet = open(input_alphabet_path, "r", encoding = "utf8").read()
else:
    print("See the list of alphabets: ")
    print(*all_files, sep='\n')
    input_alphabet_chosen = input(constants['choose_alphabet'])
    input_alphabet = open(alphabet_directory + input_alphabet_chosen, "r", encoding = "utf8").read()

if input_cipher == 'C':
    encoding_key = []
    print("Encoding key should not be longer than: " + str(len(input_alphabet)))
    encoding_key = int(input("What is your encoding key: " ))
    while encoding_key>len(input_alphabet):
        print("Encoding key should not be longer than: " + str(len(input_alphabet)))
        encoding_key = int(input("What is your encoding key: " ))

if input_cipher == 'Af':
    encoding_key1 = []
    encoding_key2 = []
    print("Encoding key1 should not be longer than: " + str(len(input_alphabet)))
    encoding_key1 = int(input("What is your encoding key1: " ))
    while encoding_key1>len(input_alphabet):
        print("Encoding key1 should not be longer than: " + str(len(input_alphabet)))
        encoding_key1 = int(input("What is your encoding key1: " ))
    print("Encoding key2 should not be longer than: " + str(len(input_alphabet)))
    encoding_key2 = int(input("What is your encoding key2: " ))
    while encoding_key2>len(input_alphabet):
        print("Encoding key2 should not be longer than: " + str(len(input_alphabet)))
        encoding_key2 = int(input("What is your encoding key2: " ))

if input_cipher == 'V':
    encoding_keyword = str(input("Please type your encoding keyword: " ))
    print(encoding_keyword)

if input_cipher == 'V':
  alphabet = {k:v for k,v in enumerate(input_alphabet)}

if input_cipher == 'C':
    message = caessar.caessar(input_text, encoding_key, input_alphabet)
    if input_encode_decode == 'E':
        result = message.encode()
    elif input_encode_decode == 'D':
        result = message.decode()

if input_cipher == 'Af':
    message = affine.affine(input_text, encoding_key1, encoding_key2, input_alphabet)
    if input_encode_decode == 'E':
        result = message.encode()
    elif input_encode_decode == 'D':
        result = message.decode()

if input_cipher == 'At':
    message = atbash.atbash(input_text, input_alphabet)
    if input_encode_decode == 'E':
        result = message.encode()
    elif input_encode_decode == 'D':
        result = message.decode()

if input_cipher == 'V':
    message = vigenere.vigenere(input_text, encoding_keyword, input_alphabet)
    if input_encode_decode == 'E':
        result = message.encode()
    elif input_encode_decode == 'D':
        result = message.decode()

results.results(input_text, input_encode_decode, input_cipher, result)
