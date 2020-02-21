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
                next_key = i % len(key)
                next_key_part = key[next_key]
                key.append(next_key_part)
        return ''.join(key)

    def encode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet)}
        vigenere_key = self.generate_key()
        for element in range(0,len(self.text)):
            for key, alpha in alphabet.items():
                if self.text[element] == alpha:
                    text_key = key
                if vigenere_key[element] == alpha:
                    sub_key = key
            total_key = text_key + sub_key
            if total_key <= len(self.text):
                letter_next = alphabet[total_key]
            else:
                letter_next = alphabet[(total_key - len(alphabet)) % len(alphabet)]
            print(letter_next)
            output.append(letter_next)
        return ''.join(output)

    def decode(self):
        output = []
        alphabet = {k:v for k,v in enumerate(self.input_alphabet)}
        vigenere_key = self.generate_key()
        for element in range(0,len(self.text)):
            for key, alpha in alphabet.items():
                if self.text[element] == alpha:
                    text_key = key
                if vigenere_key[element] == alpha:
                    sub_key = key
            total_key = text_key - sub_key
            if total_key < 0:
                letter_next = alphabet[total_key + len(alphabet)]
            else:
                letter_next = alphabet[total_key]
            output.append(letter_next)
        return ''.join(output)

