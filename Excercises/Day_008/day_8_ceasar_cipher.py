##################################################
# Python Functions with Inputs - Ceasar Cipher
##################################################

# Import the ceasar cipher artefacts
from ceasar_cipher_art import ceasar_cipher_logo

# Main variables
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Supplement functionality
def cipher(original_text, shift):
    ciphered_text = ""
    for letter in original_text:
        if letter in alphabet:
            original_letter_position = alphabet.index(letter)
            shifted_letter_position = (original_letter_position + shift) % len(alphabet)
            ciphered_text += alphabet[shifted_letter_position]
        else:
            ciphered_text += letter

    return ciphered_text

# Main functionality
def ceasar_cipher(text, shift, direction):
    if direction == "encode":
        # do nothing with the shift
        pass
    elif direction == "decode":
        shift *= -1
    else:
        return "Invalid direction. Please choose 'encode' or 'decode'."
    
    return cipher(original_text=text, shift=shift)

# User interaction
print(ceasar_cipher_logo)

is_processing = 'yes'
while is_processing == 'yes':
    encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_to_process = input("Type your message:\n").lower()
    shift_by = int(input("Type the shift number:\n"))

    print(f"The {encode_decode}d text is: '{ceasar_cipher(text=text_to_process, shift=shift_by, direction=encode_decode)}'.")

    is_processing = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
