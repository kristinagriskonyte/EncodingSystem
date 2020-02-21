class vigenere:
    def __init__(self, text, keyword, input_alphabet):
        self.text = text
        self.keyword = keyword
        self.input_alphabet = input_alphabet

    def generate_key(self):
        key = list(self.keyword)
        if len(self.text) == key:
            return key
        else:
            for i in range(len(self.text)-len(key)):
                nextKey = i % len(key)
                nextKeyPart = key[nextKey]
                key.append(nextKeyPart)
        return ''.join(key)

    def encode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet)}
        vigenere_key = self.generate_key()
        for element in range(0,len(self.text)):
            for key, alpha in alphabet.items():
                if self.text[element] == alpha:
                    textKey = key
                if vigenere_key[element] == alpha:
                    subKey = key
            totalKey = textKey + subKey
            if totalKey <= len(self.text):
                letterNext = alphabet[totalKey]
            else:
                letterNext = alphabet[(totalKey - len(alphabet)) % len(alphabet)]
            print(letterNext)
            output.append(letterNext)
        return ''.join(output)

    def decode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet)}
        vigenere_key = self.generate_key()
        for element in range(0,len(self.text)):
            for key, alpha in alphabet.items():
                if self.text[element] == alpha:
                    textKey = key
                if vigenere_key[element] == alpha:
                    subKey = key
            totalKey = textKey - subKey
            if totalKey < 0:
                letterNext = alphabet[totalKey + len(alphabet)]
            else:
                letterNext = alphabet[totalKey]
            output.append(letterNext)
        return ''.join(output)

