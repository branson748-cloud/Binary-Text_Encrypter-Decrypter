current_version = "v1.0.5"

# =========================
# TEXT TO BINARY ENCRYPTER
# =========================

def text_to_binary(text):
    binary_result = []
    for char in text:
        ascii_number = ord(char)
        binary = format(ascii_number, '08b')
        binary_result.append(binary)
    return ' '.join(binary_result)

# =========================
# BINARY TO TEXT DECRYPTER
# =========================

def binary_to_text(binary_text):
    text_result = []
    binary_list = binary_text.split()
    for binary in binary_list:
        number = int(binary, 2)
        character = chr(number)
        text_result.append(character)
    return ''.join(text_result)

# =========================
# MAIN FLOW
# =========================

print(f"Welcome to Binary-Text Encrypter/Decrypter {current_version}")

def encrypting_message(message):
    encrypted = text_to_binary(message)
    print("Encrypted message:")
    print(encrypted)
    return encrypted

def decrypting_message(binary_input):
    decrypted = binary_to_text(binary_input)
    print("Decrypted message:")
    print(decrypted)
    return decrypted

valid_choice = False

while not valid_choice:
    encrypt_or_decrypt_request = input("Please choose either to ENCRYPT or DECRYPT a message: ").strip().upper()
    if encrypt_or_decrypt_request == "ENCRYPT":
        message = input("Enter message: ")
        encrypting_message(message)
        valid_choice = False
    elif encrypt_or_decrypt_request == "DECRYPT":
        binary_input = input("Enter binary: ")
        decrypting_message(binary_input)
        valid_choice = False
    else:
        print("Invalid option. Please type in either ENCRYPT or DECRYPT.")
        valid_choice = False
