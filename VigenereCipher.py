def generateKey(text, key):
    key = list(key)
    if len(text) == key:
        return key
    else:
        for i in range(len(text)-len(key)):
            nextKey = i % len(key)
            nextKeyPart = key[nextKey]
            key.append(nextKeyPart)
    return ''.join(key)

def encodeVigenere(textToEncode, alphabet, vigenereKey):
    output = []
    for element in range(0,len(textToEncode)):
        for key, alpha in alphabet.items():
            if textToEncode[element] == alpha:
                textKey = key
            if vigenereKey[element] == alpha:
                subKey = key
        totalKey = textKey + subKey
        if totalKey <= len(textToEncode):
            letterNext = alphabet[totalKey]
        else:
            letterNext = alphabet[totalKey - len(alphabet)]
        print(letterNext)
        output.append(letterNext)
    return ''.join(output)

def decodeVigenere(textToDecode, alphabet, vigenereKey):
    output = []
    for element in range(0,len(textToDecode)):
        for key, alpha in alphabet.items():
            if textToDecode[element] == alpha:
                textKey = key
            if vigenereKey[element] == alpha:
                subKey = key
        totalKey = textKey - subKey
        if totalKey <= 0:
            letterNext = alphabet[totalKey + len(alphabet)]
        else:
            letterNext = alphabet[totalKey]
        output.append(letterNext)
    return ''.join(output)
