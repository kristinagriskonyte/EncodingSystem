class atbash:
    def __init__(self, text, input_alphabet):
        self.text = text
        self.input_alphabet = input_alphabet

    def encode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet, start=1)} 
        alphabet_reverse = {k:v for k,v in enumerate(self.input_alphabet[::-1], start=1)}
        for letter in self.text:
            key_next = 0
            for key, alpha in alphabet.items():
                if letter == alpha:
                    key_next = key
            if key_next == 0 and letter != ' ':
                print('A symbol "' + letter + '" is not found in alphabet')
                letter_next = letter
            elif letter == ' ':
                letter_next = letter
            else:
                letter_next = alphabet_reverse[key_next]
            output.append(letter_next)
        return ''.join(output)

    def decode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet, start=1)}
        alphabet_reverse = {k:v for k,v in enumerate(self.input_alphabet[::-1], start=1)}
        for letter in self.text:
            key_next = 0
            for key, alpha in alphabet_reverse.items():
                if letter == alpha:
                    key_next = key
            if key_next == 0 and letter != ' ':
                print('A symbol "' + letter + '" is not found in alphabet')
                letter_next = letter
            elif letter == ' ':
                letter_next = letter
            else:
                letter_next = alphabet[key_next]
            output.append(letter_next)
        return ''.join(output)


