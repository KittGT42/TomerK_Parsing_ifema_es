import csv
import json

import requests
from bs4 import BeautifulSoup

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
# headers_csv = ['Company_name', 'Website', 'Categories', 'Email', 'description', 'Country', 'Region', 'City', 'Stand_name', 'Stand_location',
#                'Product']
#
# with open('detailed_info_company.csv', 'w', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(headers_csv)

with open('data.json') as f:
    data = json.load(f)
count = 0
for i in data["data"]:
    count += 1
    if count < 614:
        continue
    response = requests.get(
        f'https://lc-events-web-public.ifema.es/api/v1/tenants/'
        f'3a88c5e5-a6e1-4898-b72b-103e4eed1731/editions/89eac643-8259-4a90-160a-08dbe9c30491/exhibitors/{i["id"]}',
        params=params,
        headers=headers,
    )
    res = response.json()
    Company_name = res["name"]
    Website = res["link"]
    Categories = ", ".join(res["categories"]) if res["categories"] else ""
    Email = i["email"]
    description = res["description"]
    if description:
        description = BeautifulSoup(description, 'html.parser').get_text()
    Country = res["location"]["countryCode"]
    Region = res["location"]["region"]
    City = res["location"]["city"]
    try:
        Stand_name = res["stands"][0]["name"]
    except:
        Stand_name = ''
    try:
        Stand_location = res["stands"][0]["location"]
    except:
        Stand_location = ''
    Product = ''
    with open('detailed_info_company.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([Company_name, Website, Categories, Email, description, Country, Region, City, Stand_name, Stand_location, Product])
    print(Company_name, f' {count}/{len(data["data"])} DOWLOADED')