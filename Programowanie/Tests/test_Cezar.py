import cezar

class TestCezar:
    def testEncryptLetters(self):
        c = cezar.Cezar()
        name = 'Bartek'
        encrypted_text = c.encrypt(name, 3)
        print(f'Encrypted text: {encrypted_text}')
        assert len(encrypted_text) == len(name)  # Długość szyfrowanego tekstu powinna być równa oryginalnemu
        assert encrypted_text == 'Eduwhn'  # Oczekiwany wynik szyfrowania

    def testDecryptLetters(self):
        c = cezar.Cezar()
        decrypted_text = c.decrypt('Eduwhn', 3)
        print(f'Decrypted text: {decrypted_text}')
        assert decrypted_text == 'Bartek'  # Oczekiwany wynik deszyfrowania


