alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(text, shift):
    encrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        encrypted_text += new_letter
    return encrypted_text


def decode(text, shift):
    decrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decrypted_text += new_letter
    return decrypted_text


if direction == "encode":
    print(f"The encoded text is {encode(text, shift)}")
elif direction == "decode":
    print(f"The decoded text is {decode(text, shift)}")
