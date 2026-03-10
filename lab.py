def vigenere_sq(abc):
    alphabet = list(abc)
    sq_list = [vigenere_head(abc)]
    for i in range(len(alphabet)):
        sq_list.append(list(alphabet[i]) + alphabet[i:] + alphabet[:i])
    return sq_list

def vigenere(alphabet):
    result = vigenere_sq(alpha)
    for i, row in enumerate(result):
        if i == 1:
            print(f"|{'---|' * (len(alphabet) + 1)} ")
        print(f"| {' | '.join(row)} |")

def vigenere_head(alphabet):
    a = list(alphabet)
    a.insert(0,' ')
    return a

def letter_to_index(letter:str, alphabet:str) -> int:
    if letter not in alphabet:
        raise "ERROR"
    return alphabet.find(letter)

def index_to_letter(index, alphabet):
    if not (0 <= index < len(alphabet)):
            raise "index out of bounds"
    return alphabet[index]

def vigenere_index(key_letter:str, plaintext_letter: str, alphabet:str) -> str:
    cipher_index = (letter_to_index(plaintext_letter, alphabet) + letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(cipher_index, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    key_len = len(key)
    for i, l in enumerate(plaintext):
        cipher_text.append(vigenere_index(key[i % key_len], l, alphabet))
    return ''.join(cipher_text)

def undo_vigenere(key_letter, cypher_letter, alphabet):
    pt = (letter_to_index(cypher_letter, alphabet) - letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(pt, alphabet)
alpha = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt_vigenere(key, cypher_text, alphabet):
    plaintext = []
    key_len = len(key)
    for i, l in enumerate(cypher_text):
        plaintext.append(undo_vigenere(key[i % key_len], l, alphabet))
    return ''.join(plaintext)

def main_menu(alpha, dump_list):
    menu = ['1) Encrypt', '2) Decrypt', '3) Dump']

    for item in menu:
        print(item)
    try:
        choice = int(input("Make your choice: "))
        if not 0 < choice <= len(menu):
            raise ValueError("out of range")
        if choice == 1:
            key = input("Enter your key: ")
            message = input("What message would you like to encrypt? ")
            dump_list.append(encrypt_vigenere(KEY, MESSAGE, alpha))
        if choice == 2:
            key = input("Enter your key: ")
            message = input("What message would you like to decrypt? ")
            print(decrypt_vigenere(KEY, message, alpha))
        if choice == 3:
            for ct in dump_list:
                print(ct)
    except ValueError as ve:
        print("invalid entry")

vigenere(alpha)
print(letter_to_index('z', alpha))
KEY = 'DAVINCI'
MESSAGE = 'THE EAGLE HAS LANDED'
dl = []

encrypted_str = "THE EAGLE HAS LANDED"
pt_str = decrypt_vigenere(KEY, encrypted_str, alpha)
print(MESSAGE, encrypted_str, pt_str)
main_menu(alpha, dl)