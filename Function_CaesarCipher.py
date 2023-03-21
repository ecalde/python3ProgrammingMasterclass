alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    new_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        index = alphabet.index(letter)
        new_text += alphabet[index + shift]
    print(f"The {direction}d text is {new_text}")

caesar(text, shift, direction)

# def encrypt(plain_text, shift_amount):
#     encrypt_text = ""
#     for letter in plain_text:
#         index = alphabet.index(letter)
#         encrypt_text += alphabet[index + shift_amount]
#     print(f"The encoded text is {encrypt_text}")

# def decrypt(encrypt_text, shift_amount):
#     decrypt_text = ""
#     for letter in encrypt_text:
#         index = alphabet.index(letter)
#         decrypt_text += alphabet[index - shift_amount]
#     print(f"The decoded text is {decrypt_text}")


