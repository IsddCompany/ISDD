import base64
import binascii

import isdd.callcode as cc

class IsNotISDDEncoded(Exception):
    """
    This text (or file) is not ISDD encoded
    """
    def __init__(self, message="This text (or file) is not ISDD encoded"):
        self.message = message
        super().__init__(self.message)

class IsNotISDOFile(Exception):
    """
    This text (or file) is not in the ISDO file format
    """
    def __init__(self, message="This text (or file) is not in the ISDO file format"):
        self.message = message
        super().__init__(self.message)

class TooShortToBeISDO(Exception):
    """
    This text (or file) is not long enough to be an ISDO file
    """
    def __init__(self, objectlen, message="This text (or file) is not long enough to be an ISDO file"):
        if objectlen is None:
            self.message = message
        else:
            self.message = f"{message} (len = {objectlen})"
        super().__init__(self.message)


class ISDD:
    @staticmethod
    def encoding(text: str) -> str:
        encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        hex_array = [format(ord(char), '02x') for char in encoded_text]
        return ' '.join(hex_array)

    @staticmethod
    def decoding(encoded_text: str) -> str:
        try:
            hex_array = encoded_text.split(' ')
            text = ''.join([chr(int(byte, 16)) for byte in hex_array])
            return base64.b64decode(text).decode('utf-8')
        except binascii.Error:
            raise IsNotISDDEncoded




class ISDO:
    """
    ISDO file is ISDD object file.
    This file is made up of strict rules.
    """
    def __init__(self, isddstr: str):
        try:
            hex_array = isddstr.split(' ')
            text = ''.join([chr(int(byte, 16)) for byte in hex_array])
        except ValueError:
            raise IsNotISDDEncoded

        try:
            final_text = base64.b64decode(text).decode('utf-8')
            a = final_text.split(' ')
        except binascii.Error:
            raise IsNotISDOFile

        result = [item.split(':')[1] if
                  item.startswith('GenderType:') or
                  item.startswith('Country:') else
                  item for item in a]
        try:
            if result[3] == '1':
                gender = "male"
            elif result[3] == '2':
                gender = "female"
            elif result[3] == '3':
                gender = "intersex"
            else:
                raise IsNotISDOFile
        except IndexError:
            raise TooShortToBeISDO(len(result))

        try:
            self.name = str(result[0])
            self.madeat = str(result[1])
            self.gender = str(gender)
            self.engine = str(result[2])
            self.country = str(cc.get_country_by_code(result[4]))
            self.dic = {
                'name': self.name,
                'madeyear': self.madeat,
                'gender': self.gender,
                'engine': self.engine,
                'country': self.country
            }
        except IndexError:
            raise TooShortToBeISDO(len(result))
