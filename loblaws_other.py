import requests
from rich import print
import pandas as pd

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en',
    'Business-User-Agent': 'PCXWEB',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.loblaws.ca',
    'Origin_Session_Header': 'B',
    'Referer': 'https://www.loblaws.ca/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'is-helios-account': 'false',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-apikey': 'C1xujSegT5j3ap3yexJjqhOfELwGKYvz',
    'x-application-type': 'Web',
    'x-channel': 'web',
    'x-loblaw-tenant-id': 'ONLINE_GROCERIES',
    'x-preview': 'false',
}
def json_data(index):
    json_data = {
    'cart': {
        'cartId': '000a9ba4-f9fd-4d8a-80e5-392bbb9d11bf',
    },
    'fulfillmentInfo': {
        'storeId': '1029',
        'pickupType': 'STORE',
        'offerType': 'OG',
        'date': '08062024',
        'timeSlot': None,
    },
    'listingInfo': {
        'filters': {
            'icid': [
                'gr_weekly-flyer_productcarousel_0_hp'
            ],
        },
        'sort': {},
        'pagination': {
            'from': index
        },
        'includeFiltersInResponse': False,
    },
    'banner': 'loblaw',
    'userData': {
        'domainUserId': '9e6ba2ae-342a-420c-99f4-a3bf14c4de40',
        'sessionId': '910f1791-03b0-4509-b6b8-f5846ebd3be4',
    },
    }
    return json_data



response = requests.post('https://api.pcexpress.ca/pcx-bff/api/v3/collections/featured-items', headers=headers, json=json_data(1))
# store the response of product related info in a panda data frame
dataFrame = pd.json_normalize(response.json()["layout"]["sections"]["mainContentCollection"]["components"][1]["data"]["productGrid"]["productTiles"])
print(dataFrame)

# looping through the pages, handle pagination
# for index in range(1,5):
#     response = requests.post('https://api.pcexpress.ca/pcx-bff/api/v3/collections/featured-items', headers=headers, json=json_data(index))
#     # with open(f'response{index}.txt', "w", encoding="utf-8") as f:
#         # f.write(response.json()["results"][0]["items"])
#     print(response.json()["results"][0]["items"])


# saving the dataFrame in excel
file_name = 'loblaws.xlsx'
dataFrame.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')
    