import json
import logging
import os
import sys

import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

LOGIN = 'any-login'
API_KEY = sys.argv[1]
API_URL = 'https://api.footprintnetwork.org/v1'
headers = {
    'Accept': 'application/json',
}

logging.basicConfig(level=logging.INFO)

if not os.path.isdir('data'):
    os.mkdir('data')
    os.chdir('data')

year_resp = requests.get(f'{API_URL}/years', headers=headers, auth=HTTPBasicAuth('user', API_KEY))
years = [obj['year'] for obj in json.loads(year_resp.text)]

datatypes_resp = requests.get(f'{API_URL}/types', headers=headers, auth=HTTPBasicAuth('user', API_KEY))
datatypes = [record_type['record'] for record_type in json.loads(datatypes_resp.text)]

countries = requests.get(f'{API_URL}/countries', headers=headers, auth=HTTPBasicAuth('user', API_KEY))

country_codes = [country['countryCode'] for country in json.loads(countries.text)]
country_details = {}
for country in json.loads(countries.text):
    country_details[country['countryCode']] = {'two_letter_code': country['isoa2'],
                                               'country_name': country['countryName']}

for year in years:
    country_df = []
    for country_code in country_codes:
        country_data = requests.get(f'{API_URL}/data/{country_code}/{year}', headers=headers,
                                    auth=HTTPBasicAuth('user', API_KEY))
        partial = {'country_code': country_code,
                   'country_two_letter_code': country_details[country_code]['two_letter_code'],
                   'country_name': country_details[country_code]['country_name']}
        for country_datum in json.loads(country_data.text):
            partial[country_datum['record']] = country_datum['value']
        country_df.append(partial)
    pd.DataFrame(country_df).to_csv(f'data/{year}.csv')
    logging.info(f'parsed data for {year}')
