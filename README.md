# Binary-Text Encrypter/Decrypter

A simple Python application that converts text to binary and binary back to text.

## Version
Current version: **v1.0.5**

## Features
- **Text to Binary Encrypting**: Convert any text message into its 8-bit binary representation
- **Binary to Text Decrypting**: Convert binary strings back to readable text
- **Interactive CLI**: User-friendly command-line interface for easy interaction
- **Input Validation**: Ensures users select valid options (ENCRYPT or DECRYPT)

## How It Works

### Text to Binary
The application converts each character in your text to its ASCII value, then represents that value as an 8-bit binary number.

**Example:**
```
Input:  "Hi"
Output: "01001000 01101001"
```

### Binary to Text
The application reverses the process by converting each 8-bit binary segment back to its ASCII character.

**Example:**
```
Input:  "01001000 01101001"
Output: "Hi"
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/branson748-cloud/Binary-Text_Encrypter-Decrypter.git
cd Binary-Text_Encrypter-Decrypter
```

2. Ensure you have Python 3.x installed

## Usage

Run the application:
```bash
python main.py
```

### Interactive Menu
When you run the program, you'll be prompted to choose an action:

```
Welcome to Binary-Text Encrypter/Decrypter v1.0.5
Please choose either to ENCRYPT or DECRYPT a message: 
```

**To ENCRYPT a message:**
1. Type `ENCRYPT` and press Enter
2. Enter your message when prompted
3. The binary representation will be displayed

**To DECRYPT a message:**
1. Type `DECRYPT` and press Enter
2. Enter the binary string (with spaces between 8-bit segments)
3. The decoded message will be displayed

## Example Usage

### Encryption
```
Welcome to Binary-Text Encrypter/Decrypter v1.0.5
Please choose either to ENCRYPT or DECRYPT a message: ENCRYPT
Enter message: Hello
Encrypted message:
01001000 01100101 01101100 01101100 01101111
```

### Decryption
```
Welcome to Binary-Text Encrypter/Decrypter v1.0.5
Please choose either to ENCRYPT or DECRYPT a message: DECRYPT
Enter binary: 01001000 01100101 01101100 01101100 01101111
Decrypted message:
Hello
```

## Code Structure

- **`text_to_binary(text)`**: Converts text string to binary format
  - Iterates through each character
  - Gets ASCII value using `ord()`
  - Formats as 8-bit binary using `format(ascii_number, '08b')`
  
- **`binary_to_text(binary_text)`**: Converts binary format back to text
  - Splits binary string by spaces
  - Converts each 8-bit binary to ASCII using `int(binary, 2)`
  - Reconstructs text using `chr()`

- **`encrypting_message(message)`**: User-facing function to encode text
- **`decrypting_message(binary_input)`**: User-facing function to decode binary

## Requirements
- Python 3.x
- No external dependencies

## License
This project is open source and available under the MIT License.

## Author
**branson748-cloud**

## Contributing
Feel free to fork this repository and submit pull requests for any improvements!
