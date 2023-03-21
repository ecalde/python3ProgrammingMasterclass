alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#To Do : Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    encrypt_text = ""
    #To Do : Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    for letter in plain_text:
        index = alphabet.index(letter)
        encrypt_text += alphabet[index + shift_amount]
    print(f"The encoded text is {encrypt_text}")

#To Do : Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(encrypt_text, shift_amount):
    decrypt_text = ""
  #To Do : Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    for letter in encrypt_text:
        index = alphabet.index(letter)
        decrypt_text += alphabet[index - shift_amount]
    print(f"The decoded text is {decrypt_text}")

#To Do : Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#To Do : Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("That is not a valid choice")