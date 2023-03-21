import Function_CaesarArt

print(Function_CaesarArt.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    new_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_text += alphabet[index + shift]
        else:
            new_text += char
    print(f"The {direction}d text is {new_text}")

end = False
while end == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Edge case, if user inputs a shift larger than our alphabet
    shift = shift % 26
    caesar(text, shift, direction)
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if choice == "no":
        end = True
        print("Goodbye.\n")

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


