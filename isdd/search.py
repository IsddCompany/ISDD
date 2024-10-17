import urllib.request


def getISDO(isddID:str):
    response = urllib.request.urlopen(f'https://raw.githubusercontent.com/IsddCompany/isdddatas/main/isdddatas/{isddID}.isdo')
    html = response.read()
    return html.decode('utf-8')



