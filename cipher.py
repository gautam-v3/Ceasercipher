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
youwant_continue=True
while(youwant_continue):
    choose = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    msg = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if choose == "encode":
      encrypt(msg, shift)
    elif choose == "decode":
       decrypt(msg, shift)
    else:
       print("Invalid choice.")

    conti=input("type yes to continue or else type no").lower()
    if(conti=="yes"):
        youwant_continue=True
    else:
        youwant_continue=False


