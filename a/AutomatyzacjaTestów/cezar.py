class Cezar:
    def encrypt(self, text: str, key: int):
        result = ''
        for letter in text:
            encrypted_letter = chr(ord(letter) + key)
            result += encrypted_letter
        return result

    def decrypt(self, text: str, key: int):
        return self.encrypt(text, -key)

name = 'Bartek'
c = Cezar()
print(c.encrypt(name, 3))
print(c.decrypt('Eduwhn', 3))
