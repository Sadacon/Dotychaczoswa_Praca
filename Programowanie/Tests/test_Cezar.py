import cezar


class TestCezar:
    def testEncryptLetters(self):
        c = cezar.Cezar()
        name = 'Bartek'
        encrypted_text = c.encrypt(name, key=3)
        # Długość zaszyfrowanego tekstu powinna być taka sama
        assert len(encrypted_text) == len(name)
        # Oczekiwany wynik szyfrowania
        assert encrypted_text == 'Eduwhn'

    def testDecryptLetters(self):
        c = cezar.Cezar()
        decrypted_text = c.decrypt(
            text='Eduwhn', key=3
        )
        # Oczekiwany wynik deszyfrowania
        assert decrypted_text == 'Bartek'
