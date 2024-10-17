import base64
import callcode as cc

class Isdo:
    def __init__(self, isddstr: str):
        data = isddstr
        hex_array = data.split(' ')
        text = ''.join([chr(int(byte, 16)) for byte in hex_array])
        final_text = base64.b64decode(text).decode('utf-8')
        a = final_text.split(' ')
        result = [item.split(':')[1] if item.startswith('GenderType:') or item.startswith('Country:') else item for item
                  in a]

        if result[3] == '1':
            gender = "남성"
        elif result[3] == '2':
            gender = "여성"
        elif result[3] == '3':
            gender = "간성"
        else:
            gender = None

        self.name = result[0]
        self.madeat = result[1]
        self.gender = gender
        self.engine = result[2]
        self.country = cc.get_country_code(result[4])

