import urllib.request


def get_isdd_object(isddid:str):
    response = urllib.request.urlopen(
        f'https://raw.githubusercontent.com/IsddCompany/isdddatas/main/isdddatas/{isddid}.isdo'
    )
    html = response.read()
    return html.decode('utf-8')



