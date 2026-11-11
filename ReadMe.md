# Caesar Cipher CLI 🔐

A Python command-line tool that encrypts and decrypts messages using the classic **Caesar Cipher** substitution technique. 

## ✨ Features
- **Encode & Decode:** Shift letters forward to encrypt or backward to decrypt.
- **Alphabet Wrap-Around:** Uses modulo arithmetic (`% 26`) so shifts past `'z'` cleanly wrap back to `'a'`.
- **Preserves Formatting:** Keeps spaces, numbers, and punctuation intact without crashing.
- **Handles Large Shifts:** Works seamlessly even if the shift value exceeds 26.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation & Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/gautam-v3/Caesar-Cipher.git](https://github.com/gautam-v3/Caesar-Cipher.git)
   cd Caesar-Cipher
   ```
2. Run the script:
   ```bash
   python caesar_cipher.py
   ```

## 💻 Example Run

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
5
Here is the encoded result: mjqqt btwqi!
```

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt btwqi!
Type the shift number:
5
Here is the decoded result: hello world!
```

## 🧠 How It Works
Each alphabetic character in the input string is located in `string.ascii_lowercase` and shifted by `n` positions using:

$$\text{new index} = (\text{current index} \pm \text{shift}) \bmod 26$$

Non-alphabetic characters (spaces, symbols, digits) bypass the shift and are appended directly to the output.
