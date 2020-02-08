def results(text, inputEncodeDecode, Cipher, result): 
    print("Yout text given:", ''.join(text))
    if inputEncodeDecode == 'E':
        print("Your text has been encrypted")
    elif inputEncodeDecode == 'D':
        print("Your text has been decrypted")
    elif inputEncodeDecode == 'B':
        print("Your text has been brute forced")
    if Cipher == 'C':
        print("Caessar cipher was used")
    elif Cipher == 'At':
        print("Atbach cipher was used")
    elif Cipher == 'Af':
        print("Affine cipher was used")
    elif Cipher == 'V':
        print("Vigenere cipher was used")
    print("Your result is:", result)
    print("Here is" , len(text) , "symbols in given text")