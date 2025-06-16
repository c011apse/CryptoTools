from collections import Counter
from functools import reduce
from cipher import VigenereCipher

class VigenereCracker:
    def __init__(self, ciphertext=None) -> None:
        self.ciphertext = ciphertext.upper() if ciphertext else ""
        self.ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.freqs = {
            'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253,
            'E': 0.12702, 'F': 0.02228, 'G': 0.02015, 'H': 0.06094,
            'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025,
            'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929,
            'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
            'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150,
            'Y': 0.01974, 'Z': 0.00074
        }
    def clean_text(self, text: str) -> str:
        return ''.join(letter for letter in text if letter in self.ALPHABET)
    
    # Поиск повторяющихся последовательностей в тексте
    def find_repeated_sequence(self, min_len=3):
        sequences = {}
        text = self.clean_text(text=self.ciphertext)

        for length in range(min_len, 6):
            for i in range(len(text) - length + 1):
                seq = text[i:i + length]
                if seq in sequences:
                    sequences[seq].append(i)
                else:
                    sequences[seq] = [i]
        
        return {seq: positions for seq, positions in sequences.items() if len(positions) > 1}
    
    # KASISKI METHOD
    def get_key_length(self): 
        sequences = self.find_repeated_sequence()
        distances = []

        for seq, positions in sequences.items():
            for i in range(len(positions) - 1):
                distances.append(positions[i + 1] - positions[i])

        if not distances:
            return None
        
        def get_div(n):
            return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        
        all_divisors = []
        for div in distances:
            divisors = get_div(div)
            all_divisors.extend(d for d in divisors if d > 1)

        return Counter(all_divisors).most_common(1)[0][0]
    
    # FREQUENCY ANALYSIS
    def frequerncy_analysis(self, sequence):
        scores = []
        for shift in range(26):
            decrypted = ''.join( self.ALPHABET[(self.ALPHABET.index(c) - shift) %26] for c in sequence )
            score = sum(self.freqs.get(char,0) * decrypted.count(char) for char in self.ALPHABET)
            scores.append((shift, score))

        return max(scores, key=lambda x: x[1])[0]
    
    def crack_key(self):
        if len(self.clean_text(self.ciphertext)) < 50:
            print("Warning: Text is too short for reliable analysis")

        key_length = self.get_key_length()
        if not key_length:
            return None
        
        text = self.clean_text(self.ciphertext)
        key = []

        for i in range(key_length):
            sequence = text[i::key_length]
            shift = self.frequerncy_analysis(sequence)
            key.append(self.ALPHABET[shift])
        
        return ''.join(key)
    
    def decrypt(self, key):
        cipher = VigenereCipher(key)
        return cipher.decrypt(self.ciphertext)