# Math Ciphers

## Overview
Math Ciphers is a Python module that provides classes for encryption and decryption using mathematical ciphers.

## Features
- Implements a base cipher class for creating mathematical ciphers.
- Provides methods for encryption and decryption using the base cipher.
- Supports customizable configuration, keyword, and block size for encryption.

## Installation
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Inshasi/Math_Cipher.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Math_cipher
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Import the `Base_Cipher` class from the `math_ciphers` module:

    ```python
    from math_ciphers import Base_Cipher
    ```

2. Create an instance of `Base_Cipher` with an optional key:

    ```python
    cipher = Base_Cipher()
    ```

3. Encrypt plaintext using the `encrypt` method:

    ```python
    plaintext = "Hello, world!"
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:", ciphertext)
    ```

4. Decrypt ciphertext using the `decrypt` method:

    ```python
    decrypted_text = cipher.decrypt(ciphertext)
    print("Decrypted text:", decrypted_text)
    ```

## Documentation
- `Base_Cipher` class:
    - `__init__(key)`: Constructor for the cipher class. Initializes the cipher with an optional key.
    - `encrypt(plaintext)`: Encrypts the given plaintext.
    - `decrypt(ciphertext)`: Decrypts the given ciphertext.
    - Additional methods for setting and getting the cipher's key, configuration, and more.

## Examples
1. Encrypting and Decrypting Text:
   
    ```python
    cipher = Base_Cipher()
    plaintext = "Hello, world!"
    ciphertext = cipher.encrypt(plaintext)
    decrypted_text = cipher.decrypt(ciphertext)
    ```

2. Customizing Configuration and Keyword:

    ```python
    custom_key = (('A', 'Z', 3), 'KEYWORD')
    cipher.set_key(custom_key)
    ```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for feature requests, bug fixes, or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
