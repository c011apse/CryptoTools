import logo

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class CaesarCipher:
    def __init__(self, rot=0):
        self.rot = rot


    def encrypt(self, text: str) -> str:
        encrypted_text = []
        for letter in text:
            if letter.lower() in ALPHABET:
                index_letter = ALPHABET.find(letter.lower())
                if letter in ALPHABET.upper():
                    encrypted_text.append(ALPHABET[ (index_letter + self.rot) % len(ALPHABET) ].upper())
                else:
                    encrypted_text.append(ALPHABET[ (index_letter + self.rot) % len(ALPHABET) ])
            # another sybmols
            else:
                encrypted_text.append(letter)
        
        return ''.join(encrypted_text)


    def decrypt(self, text: str) -> str:
        decrypted_text = []
        for letter in text:
            if letter.lower() in ALPHABET:
                index_letter = ALPHABET.find(letter.lower())
                if letter in ALPHABET.upper():
                    decrypted_text.append(ALPHABET[ index_letter - self.rot ].upper())
                else:
                    decrypted_text.append(ALPHABET[ index_letter - self.rot ])
            # another sybmols
            else:
                decrypted_text.append(letter)
                
        return ''.join(decrypted_text)


def choice_rot():
    while True:
        try:
            shift = int(input("CHOOSE SHIFT (1-25): "))
            if 1<= shift <= 25:
                return shift
            else: print("SHIFT MUST BE BETWEEN 1 AND 25")
        except ValueError:
            print('ENTER NUMBER!')

##### [ INTERFACE ] #####
print(logo.art)
def main():
    cipher = CaesarCipher()

    while True:
        print("MENU:\n[1] ENCRYPT\n[2] DECRYPT\n[3] BRUTE-FORCE\n\n[0] EXIT")
        choice = input("SELECT ACTION: ")

        if choice == '1':
            text = input("ENTER TEXT TO ENCRYPT: ")
            cipher.rot = choice_rot()
            encrypted = cipher.encrypt(text)
            print(f"\nENCRYPTED TEXT -> {encrypted}\n" )
            
        elif choice == '2':
            text = input("ENTER TEXT TO DECRYPT: ")
            cipher.rot = choice_rot()
            decrypted = cipher.encrypt(text)
            print(f"\nDECRYPTED TEXT -> {decrypted}\n")

        elif choice == '3':
            text = input("ENTER TEXT: ")
            print()
            for i in range(1, len(ALPHABET)):
                cipher.rot = i
                crypted = cipher.decrypt(text)
                print(f"[ {i} ] [ {crypted} ]")
            print()

        elif choice == '0':
            print("BYE-BYE!")
            break

        else: print("INCORRECT CHOICE. ENTER 1, 2, 3 or 0")

        input('\nPRESS "ENTER" TO CONTINUE')

if __name__ == '__main__':
    main()
