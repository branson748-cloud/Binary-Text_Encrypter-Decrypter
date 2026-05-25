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

current_version = "v1.0.3"

print(f"Welcome to Binary-Text Encrypter/Decrypter {current_version}")

def encoding_message(message):
    encoded = text_to_binary(message)
    print("Encoded:")
    print(encoded)
    return encoded


def decoding_message(binary_input):
    decoded = binary_to_text(binary_input)
    print("Decoded message:")
    print(decoded)
    return decoded

valid_choice = False

while not valid_choice:
    encode_or_decode_request = input("Please either to ENCRYPT or DECRYPT a message: ").strip().upper()
    if encode_or_decode_request == "ENCRYPT":
        message = input("Enter message: ")
        encoding_message(message)
        valid_choice = True
    elif encode_or_decode_request == "DECRYPT":
        binary_input = input("Enter binary: ")
        decoding_message(binary_input)
        valid_choice = True
    else:
        print("Invalid option. Please choose either ENCRYPT or DECRYPT.")
        valid_choice = False
