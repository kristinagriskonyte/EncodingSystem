def results(text, input_encode_decode, cipher, result): 
    print("Yout text given:", ''.join(text))
    if input_encode_decode == 'E':
        print("Your text has been encrypted")
    elif input_encode_decode == 'D':
        print("Your text has been decrypted")
    elif input_encode_decode == 'B':
        print("Your text has been brute forced")
    if cipher == 'C':
        print("Caessar cipher was used")
    elif cipher == 'At':
        print("Atbach cipher was used")
    elif cipher == 'Af':
        print("Affine cipher was used")
    elif cipher == 'V':
        print("Vigenere cipher was used")
    print("Your result is:", result)
    print("Here is" , len(text) , "symbols in given text")
