import json

import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,uk-UA;q=0.7,uk;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.ifema.es',
    'Referer': 'https://www.ifema.es/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'language': 'en-GB',
}

json_data = {
    'page': 0,
    'pageSize': 10000,
    'search': '',
    'dynamicFields': [],
    'countryIds': [],
}

response = requests.post(
    'https://lc-events-web-public.ifema.es/api/v1/tenants/3a88c5e5-a6e1-4898-b72b-103e4eed1731/editions/89eac643-8259-4a90-160a-08dbe9c30491/exhibitors/search',
    params=params,
    headers=headers,
    json=json_data,
)

data = response.json()
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)