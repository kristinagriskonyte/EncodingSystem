def cipher_directory(cipher):
    switcher = {
        'C':'caessar/',
        'At':'atbash/',
        'Af':'affine/',
        'V': 'vigenere/'
    }
    return switcher.get(cipher)