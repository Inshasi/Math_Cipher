# ------------------------
# Math Ciphers
# ------------------------
import utilities
# ------------------------

from utilities import get_chars
import math


class Base_Cipher:
    ALPHABET = get_chars('lower') + get_chars('uppernum')
    DEFAULT_KEY = (('A', 'Z', 5), 'CRYPT')

    def __init__(self, key=DEFAULT_KEY):
        """
        ----------------------------------------------------
        Base_Cipher Constructor
        Parameters:   key (tuple):
                        (config (tuple), keyword (str)
        Description:  Constrct a cipher_base object
                      Has one private property: __key
                      If given key is valid --> set key to given value
                      otherwise, set key to DEFAULT_KEY
        ----------------------------------------------------
        """
        if self.valid_key(key):
            self.__key = key
        else:
            self.__key = self.DEFAULT_KEY
        pass

    def __str__(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       output (str)
        Description:  Creates a string representation of Base_Cipher objects
                      Format: y = x + <keyword> mod <m>
        ----------------------------------------------------
        """
        return 'y = x + {} mod {}'.format(self.__key[1], self.get_mod())

    @staticmethod
    def valid_configuration(config):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   input(?)
        Return:       True/False
        Description:  Check if given configuration is valid
                      A valid configuration is a tuple of 3 items
                      First item is a single character in ALPHABET
                      Second item is a single character in ALPHABET
                          which is after First
                      Third item is a positive integer
        ----------------------------------------------------
        """
        if type(config) == tuple and len(config) == 3:
            if type(config[0]) == str and type(config[1]) == str and type(config[2]) == int and len(
                    config[0]) == 1 and len(config[1]) == 1:
                if Base_Cipher.ALPHABET.find(config[0]) != -1 and Base_Cipher.ALPHABET.find(config[1]) != -1:
                    if 0 <= Base_Cipher.ALPHABET.index(config[0]) < Base_Cipher.ALPHABET.index(config[1]) and config[
                        2] > 0:
                        return True
        return False

    @staticmethod
    def get_alphabet(config):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   input(?)
        Return:       alphabet (str)
        Description:  Return corresponding alphabet for a given configuration
                      The alphabet is a subset of ALPHABET
                      If invalid config return empty string
        ----------------------------------------------------
        """
        if Base_Cipher.valid_configuration(config):
            st = Base_Cipher.ALPHABET.index(config[0])
            ed = Base_Cipher.ALPHABET.index(config[1])
            return Base_Cipher.ALPHABET[st:ed + 1]
        else:
            return ''

    @staticmethod
    def valid_key(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key(?)
        Return:       True/False
        Description:  Check if given arg is a valid Base_Cipher key
                      A valid key is a tuple consisting of 2 elements
                      (config,keyword)
                      The config should be a valid configuration
                      The keyword should be:
                          1- A string
                          2- All characters defined in the alphabet
                          3- Smaller than the block size
        ----------------------------------------------------
        """
        if type(key) == tuple and len(key) == 2:
            if Base_Cipher.valid_configuration(key[0]):
                if type(key[1]) == str and len(key[1]) <= key[0][2]:
                    for i in key[1]:
                        if Base_Cipher.ALPHABET.index(key[0][0]) <= Base_Cipher.ALPHABET.index(
                                i) <= Base_Cipher.ALPHABET.index(key[0][1]):
                            continue
                        else:
                            return False
                    return True
        return False

    def get_key(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       key (tuple)
        Description:  Returns a copy of key
        ----------------------------------------------------
        """
        return self.__key

    def set_key(self, key):
        """
        ----------------------------------------------------
        Parameters:   key(?)
        Return:       True/False
        Description:  set key to given argument
                      If valid --> set key and return True
                      otherwise --> set key to DEFAULT_KEY and return False
        ----------------------------------------------------
        """
        if Base_Cipher.valid_key(key):
            self.__key = key
            return True
        else:
            self.__key = self.DEFAULT_KEY
            return False

    def get_base(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       base (int)
        Description:  Computes and returns the mathematical base
                      For example: lowercase alphabet --> 26
        ----------------------------------------------------
        """
        return len(self.get_alphabet(self.__key[0]))

    def get_mod(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       mod (str)
        Description:  Computes and returns the mod for the cipher
                      For example: lowercase with block size = 5 --> baaaaa
        ----------------------------------------------------
        """
        return self.get_alphabet(self.__key[0])[1] + self.get_alphabet(self.__key[0])[0] * self.__key[0][2]

    def preprocess(self, plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext(str)
        Return:       modified_text (str)
                      positions (2D list)
        Description:  Formats the given plaintext by:
                        1- Remove unused characters
                        2- Pad, if necessary, with last character in alphabet
        ----------------------------------------------------
        """
        st = self.ALPHABET.index(self.__key[0][0])
        ed = self.ALPHABET.index(self.__key[0][1])
        b = self.get_alphabet(self.__key[0])
        unused = ''
        for i in range(len(plaintext)):
            if plaintext[i] not in b:
                unused += plaintext[i]
        position = utilities.get_positions(plaintext, unused)
        plaintext = utilities.clean_text(plaintext, unused)
        while True:
            l = len(plaintext)
            if l / self.__key[0][2] == int(l / self.__key[0][2]):
                break
            else:
                plaintext += b[-1]
        return plaintext, position

    def encode(self, block):
        """
        ----------------------------------------------------
        Parameters:   block(str)
        Return:       code (int)
        Description:  Converts a given text into a code (integer) in
                      the given base
                      For example, in base = 26
                      A --> 0
                      BA --> 26
        ----------------------------------------------------
        """
        if type(block) != str:
            return -1
        l = len(block)
        basee = self.get_alphabet(self.__key[0])
        lbasee = self.get_base()
        cd = 0
        i = l - 1
        p = 0
        while i >= 0:
            if basee.find(block[i]) == -1:
                i -= 1
                continue
            cd += basee.index(block[i]) * (lbasee ** p)
            i -= 1
            p += 1
        return cd

    def decode(self, number):
        """
        ----------------------------------------------------
        Parameters:   code(int)
        Return:       text (str)
        Description:  Converts a given code (integer) to text in the given base
                      For example, in base = 26
                      0 --> A
                      26 --> BA
        ----------------------------------------------------
        """
        if type(number) != int:
            return -1
        code = number
        if code == 0:
            return "A"
        r = ""
        while code > 0:
            temp = code % self.get_base()
            r = self.get_alphabet(self.__key[0])[temp] + r
            code = code // self.get_base()
        return r

    def encrypt(self, plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext(str)
        Return:       ciphertext (str)
        Description:  Encrypts given plaintext using Base_Cipher
        ----------------------------------------------------
        """
        p = self.preprocess(plaintext)
        textt = utilities.text_to_blocks(p[0], self.__key[0][2])
        y = ''
        c = 0
        mod = self.encode(self.get_mod())
        k = self.encode(self.__key[1])
        for i in textt:
            c = (self.encode(i) + k) % mod
            y += self.decode(c)

        y = utilities.insert_positions(y, p[1])
        return y

    def decrypt(self, ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext(str)
        Return:       plaintext(str)
        Description:  Decrypts given ciphertext using Base_Cipher
        ----------------------------------------------------
        """
        ccc = ''
        for i in range(len(ciphertext)):
            if ciphertext[i] not in self.get_alphabet(self.__key[0]):
                ccc += ciphertext[i]
        pos = utilities.get_positions(ciphertext, ccc)
        ciphertext = utilities.clean_text(ciphertext, ccc)

        textt = utilities.text_to_blocks(ciphertext, self.__key[0][2])
        y = ''
        c = 0
        mod = self.encode(self.get_mod())
        k = self.encode(self.__key[1])
        for i in textt:
            c = (self.encode(i) - k) % mod
            y += self.decode(c)

        y = utilities.insert_positions(y, pos)
        for i in range(len(y)):
            if self.get_alphabet(self.__key[0])[-1] == y[len(y) - i - 1]:
                y = y[:-1]

        return y
