# da pro4eta kakvo e api
import requests


URL = 'https://api.instantwebtools.net/v1/passenger?page={page}&size={size}'


def list_all_passangers():
    size = 20
    page = 0
    total_pages = None

    while True:
        if page == total_pages:
            break
        url = URL.format(page=page, size=size)
        response = requests.get(url)
        data = response.json()
        total_pages = data['totalPages']
        for passanger in data['data']:
            yield passanger
        page += 1


for p in list_all_passangers():
    print(p['name'])