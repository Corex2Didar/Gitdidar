def vigenere_encrypt(text, key):
    enc_text = ""
    key_length = len(key)

    for i, char in enumerate(text):
        if char.isalpha():
            key_shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                enc_char = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            else:
                enc_char = chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
            enc_text += enc_char
        else:enc_text += char
    return enc_text

def vigenere_decrypt(ciphertext, key):
    dec_text = ""
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                dec_char = chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
            else:
                dec_char = chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
            dec_text += dec_char
        else:dec_text += char
    return dec_text

text = "didarisnotsick"
key = "KEY"

enc_text = vigenere_encrypt(text, key)
print("Encrypted text:", enc_text)

dec_text = vigenere_decrypt(enc_text, key)
print("Decrypted text:", dec_text)
