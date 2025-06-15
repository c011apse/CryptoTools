import logo

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class AtbashCipher:
    def __init__(self):
        pass

    def cipher(self, text: str) -> str:
        result = []

        for letter in text:
            if letter.lower() in ALPHABET:
                index = ALPHABET.find(letter.lower()) + 1
                if letter in ALPHABET.upper():
                    result.append(ALPHABET[-index].upper())
                else:
                    result.append(ALPHABET[-index])
            # another symbols
            else: result.append(letter)
        return ''.join(result)
print(logo.art)
def run():
    Cipher = AtbashCipher()

    while True:
        print("[1] ENCRYPT / DECRYPT\n[0] EXIT")
        choice = input("-> ")

        if choice == '1':
            text = input("ENTER YOUR TEXT: ")
            encrypted_text = Cipher.cipher(text)
            print(f'\nRESULT -> {encrypted_text}\n')
        elif choice == '0':
            print("BYE!")
            break
        else: print("INCORRECT CHOICE. ENTER 1 or 0")

        input('PRESS "ENTER" TO CONTINUE')

if __name__ == '__main__':
    run()


