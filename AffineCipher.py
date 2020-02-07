class Affine:
    def __init__(self, text, keyA, keyB, inputAlphabet):
        self.text = text
        self.keyA = keyA
        self.keyB = keyB
        self.inputAlphabet = inputAlphabet

    def encode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.inputAlphabet)}
        for letter in self.text:
            for key, alpha in alphabet.items():
                if letter == alpha:
                    keyNext = (key * self.keyA + self.keyB) % len(alphabet)
                    letterNext = alphabet[keyNext]
            output.append(letterNext)
        return ''.join(output)

    def decode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.inputAlphabet)}
        for letter in self.text:
            for key, alpha in alphabet.items():
                if letter == alpha:
                    keyNext = ((len(alphabet) - self.keyA) * (key - self.keyB) ) % len(alphabet)
                    letterNext = alphabet[keyNext]
            output.append(letterNext)
        return ''.join(output)


