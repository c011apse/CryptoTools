ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class VigenereCipher:
    def __init__(self, key):
        self.key = key.lower()

# # # # # # # # # # [ ENCRYPT ] # # # # # # # # # #
    def encrypt(self, text: str) -> str:
        text = [char for char in text if char!=" " and char.lower() in ALPHABET]
        encrypted = []
        key_pos = 0
        for i, letter in enumerate(text): # <- ПРОБЛЕМА С ПРОБЕЛАМИ!
            if letter in ALPHABET:
                letter_key = self.key[i % len(self.key)]
                index_key = ALPHABET.find(letter_key)
                index_letter = ALPHABET.find(letter)
                encrypted.append(ALPHABET[ (index_letter + index_key) % len(ALPHABET) ])
            elif letter in ALPHABET.upper():
                letter_key = self.key[i % len(self.key)]
                index_key = ALPHABET.find(letter_key)
                index_letter = ALPHABET.find(letter.lower())
                encrypted.append(ALPHABET[ (index_letter + index_key) % len(ALPHABET) ].upper())
            else:
                encrypted.append(letter)

        return ''.join(encrypted)
    
# # # # # # # # # # [ DECRYPT ] # # # # # # # # # #
    def decrypt(self, text: str) -> str:
        text = [char for char in text if char!=" " and char.lower() in ALPHABET]
        decrypted = []
        for i, letter in enumerate(text): # <- ПРОБЛЕМА С ПРОБЕЛАМИ!
            if letter in ALPHABET:
                letter_key = self.key[i % len(self.key)]
                index_key = ALPHABET.find(letter_key)
                index_letter = ALPHABET.find(letter)
                decrypted.append(ALPHABET[ (index_letter - index_key) % len(ALPHABET) ])
            elif letter in ALPHABET.upper():
                letter_key = self.key[i % len(self.key)]
                index_key = ALPHABET.find(letter_key)
                index_letter = ALPHABET.find(letter.lower())
                decrypted.append(ALPHABET[ (index_letter - index_key) % len(ALPHABET) ].upper())
            else:
                decrypted.append(letter)

        return ''.join(decrypted)
