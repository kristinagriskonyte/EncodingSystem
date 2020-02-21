class caessar:
    def __init__(self, text, key, input_alphabet):
        self.text = text
        self.key = key
        self.input_alphabet = input_alphabet

    def encode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet, start=1)}
        for letter in self.text:
            key_next = 0
            for element, alpha in alphabet.items():
                if letter == alpha:
                    key_next = element + self.key
            if key_next == 0 and letter != ' ':
                print('A symbol "' + letter + '" is not found in alphabet')
            if key_next > len(alphabet):      
                key_next = key_next - len(alphabet) 
            if key_next == 0:
                letter_next = letter
            else:
                letter_next = alphabet[key_next]
            output.append(letter_next)
        return ''.join(output)

    def decode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet, start=1)}
        for letter in self.text:
            key_next = 0
            key_changed = 0
            for element, alpha in alphabet.items():
                if letter == alpha:
                    key_next = element - self.key
                    key_changed = 1
            if key_next == 0 and key_changed != 1 and letter != ' ':
                print('A symbol "' + letter + '" is not found in alphabet')
            if key_next <= 0 and key_changed == 1:
                key_next = key_next + len(alphabet)
            if key_next == 0 and key_changed != 1:
                letter_next = letter
            else:
                letter_next = alphabet[key_next]
            output.append(letter_next)
        return ''.join(output)


