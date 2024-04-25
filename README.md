# Math Ciphers

## Overview
The Math Ciphers project provides a Python implementation of a base cipher, which is a simple encryption and decryption algorithm based on mathematical operations. This cipher operates on a given alphabet and a keyword, allowing you to encode and decode messages.

## Getting Started
To use the Math Ciphers module, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.6 or later).
3. Import the `Base_Cipher` class from `math_ciphers.py` in your Python script or interactive environment.

```python
from math_ciphers import Base_Cipher

# Create a cipher with the default key
cipher = Base_Cipher()

# Create a cipher with a custom key
custom_key = (('A', 'Z', 5), 'CRYPT')
cipher = Base_Cipher(custom_key)
