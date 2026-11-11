import string

letters = list(string.ascii_letters)

def encrypt(msg, shift):
    encrypted_msg = ""
    for letter in msg:
        if letter in letters:
            letter_index = (letters.index(letter) + shift) % len(letters)
            encrypted_msg += letters[letter_index]
        else:
            encrypted_msg += letter
    print(f"Here is the encoded result: {encrypted_msg}")

def decrypt(msg, shift):
    decrypted_msg = ""
    for letter in msg:
        if letter in letters:
            letter_index = (letters.index(letter) - shift) % len(letters)
            decrypted_msg += letters[letter_index]
        else:
            decrypted_msg += letter
    print(f"Here is the decoded result: {decrypted_msg}")

choose = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
msg = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if choose == "encode":
    encrypt(msg, shift)
elif choose == "decode":
    decrypt(msg, shift)
else:
    print("Invalid choice.")