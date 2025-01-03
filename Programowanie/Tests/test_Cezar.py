from cezar import Cezar

class TestCezar:
    def testEncryptLetters(self):
        c = Cezar()
        name = 'Bartek'
        encrypted_text = c.encrypt(name, key=3)
        assert len(encrypted_text) == len(name)  # Długość zaszyfrowanego tekstu powinna być taka sama
        assert encrypted_text == 'Eduwhn'       # Oczekiwany wynik szyfrowania

    def testDecryptLetters(self):
        c = Cezar()
        decrypted_text = c.decrypt(text='Eduwhn', key=3)
        assert decrypted_text == 'Bartek'       # Oczekiwany wynik deszyfrowania
