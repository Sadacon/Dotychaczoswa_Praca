class Cezar:
    def encrypt(self, text: str, key: int) -> str:
        result = ''
        for letter in text:
            encrypted_letter = chr(ord(letter) + key)
            result += encrypted_letter
        return result

    def decrypt(self, text: str, key: int) -> str:
        return self.encrypt(text, -key)
