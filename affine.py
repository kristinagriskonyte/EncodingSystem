class affine:
    def __init__(self, text, key_a, key_b, input_alphabet):
        self.text = text
        self.key_a = key_a
        self.key_b = key_b
        self.input_alphabet = input_alphabet

    def encode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet)}
        for letter in self.text:
            for key, alpha in alphabet.items():
                if letter == alpha:
                    key_next = (key * self.key_a + self.key_b) % len(alphabet)
                    letter_next = alphabet[key_next]
            output.append(letter_next)
        return ''.join(output)

    def decode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet)}
        for letter in self.text:
            for key, alpha in alphabet.items():
                if letter == alpha:
                    key_next = ((len(alphabet) - self.key_a) * (key - self.key_b) ) % len(alphabet)
                    letter_next = alphabet[key_next]
            output.append(letter_next)
        return ''.join(output)


