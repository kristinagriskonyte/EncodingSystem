class Caessar:
    def __init__(self, text, key, inputAlphabet):
        self.text = text
        self.key = key
        self.inputAlphabet = inputAlphabet

    def encode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.inputAlphabet, start=1)}
        for letter in self.text:
            keyNext = 0
            for element, alpha in alphabet.items():
                if letter == alpha:
                    keyNext = element + self.key
            if keyNext == 0 and letter != ' ':
                print('A symbol "' + letter + '" is not found in alphabet')
            if keyNext > len(alphabet):      
                keyNext = keyNext - len(alphabet) 
            if keyNext == 0:
                letterNext = letter
            else:
                letterNext = alphabet[keyNext]
            output.append(letterNext)
        return ''.join(output)

    def decode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.inputAlphabet, start=1)}
        for letter in self.text:
            keyNext = 0
            keyChanged = 0
            for element, alpha in alphabet.items():
                if letter == alpha:
                    keyNext = element - self.key
                    keyChanged = 1
            if keyNext == 0 and keyChanged != 1 and letter != ' ':
                print('A symbol "' + letter + '" is not found in alphabet')
            if keyNext <= 0 and keyChanged == 1:
                keyNext = keyNext + len(alphabet)
            if keyNext == 0 and keyChanged != 1:
                letterNext = letter
            else:
                letterNext = alphabet[keyNext]
            output.append(letterNext)
        return ''.join(output)


