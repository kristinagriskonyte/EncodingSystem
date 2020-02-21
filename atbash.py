class Atbash:
    def __init__(self, text, input_alphabet):
        self.text = text
        self.input_alphabet = input_alphabet

    def encode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet, start=1)} 
        alphabetReverse = {k:v for k,v in enumerate(self.input_alphabet[::-1], start=1)}
        for letter in self.text:
            keyNext = 0
            for key, alpha in alphabet.items():
                if letter == alpha:
                    keyNext = key
            if keyNext == 0 and letter != ' ':
                print('A symbol "' + letter + '" is not found in alphabet')
                letterNext = letter
            elif letter == ' ':
                letterNext = letter
            else:
                letterNext = alphabetReverse[keyNext]
            output.append(letterNext)
        return ''.join(output)

    def decode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet, start=1)}
        alphabetReverse = {k:v for k,v in enumerate(self.input_alphabet[::-1], start=1)}
        for letter in self.text:
            keyNext = 0
            for key, alpha in alphabetReverse.items():
                if letter == alpha:
                    keyNext = key
            if keyNext == 0 and letter != ' ':
                print('A symbol "' + letter + '" is not found in alphabet')
                letterNext = letter
            elif letter == ' ':
                letterNext = letter
            else:
                letterNext = alphabet[keyNext]
            output.append(letterNext)
        return ''.join(output)

