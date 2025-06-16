from cipher import VigenereCipher
from cracker import VigenereCracker
from logo import art

def get_key():
    while True:
        try:
            key = input("YOUR KEY: ")
            if not key.isalpha():
                raise ValueError
            return key
        except ValueError:
            print("ONLY LETTERS!")

print(art)
def run():
    while True:
        print("[1] ENCRYPT\n[2] DECRYPT\n[3] HACK\n\n[0] EXIT")
        choice = input()

        if choice == '1':             # <- ENCRYPT
            text = input("WRITE THE TEXT: ")
            key = get_key()
            cipher = VigenereCipher(key)
            encrypted_text = cipher.encrypt(text)
            print(f"YOUR ENCRYPTED TEXT -> {encrypted_text}")

        elif choice == '2':           # <- DECRYPT
            encrypted_text = input("ENCRYPTED TEXT: ")
            key = get_key()
            cipher = VigenereCipher(key)
            decrypted_text = cipher.decrypt(encrypted_text)
            print(f"YOUR DECRYPTED TEXT -> {decrypted_text}")

        elif choice == '3':           # <- HACk
            encrypted_text = input("ENCRYPTED TEXT: ")
            cracker = VigenereCracker(encrypted_text)
            print("\nTEXT ANALYSIS...\n")
            key = cracker.crack_key()

            if key:
                print(f"KEY -> {key}")
                decrypted = cracker.decrypt(key)
                print(f"DECRYPTED TEXT -> {decrypted}")
            else:
                print("FAILED TO DETECT KEY. TEXT MAY BE TOO SHORT.")

        elif choice == '0':           # <- EXIT
            print("BYE-BYE")
            break

        else: print("INCORRECT CHOICE. ENTER 1, 2 or 0")
        input('\nPRESS "ENTER" TO CONTINUE...\n')
    

if __name__ == '__main__':
    run()