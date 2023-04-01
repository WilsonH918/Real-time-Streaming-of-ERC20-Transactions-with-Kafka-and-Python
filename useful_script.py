import requests
from datetime import datetime
import json
import csv
import pandas as pd


def get_token_data():
    # Set API key and ERC-20 token address
    api_key = 'YOUR_API_KEY'
    contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'  # Replace with the contract address that you wish to observe

    api_endpoint = 'https://api.etherscan.io/api'
    api_params = {
        'module': 'account',
        'action': 'tokentx',
        'contractaddress': contract_address,
        'sort': 'desc',  # Sort transactions (most recent for 'desc')
        'offset': 1,  # Set number of records get from page (most recent '10' records)
        'page': 1,  # Set page number (most recent page)
        'apikey': api_key
    }

    # Get a List of data
    response = requests.get(api_endpoint, params=api_params)
    data = response.json()

    return data

def transform_token_data(json_data):
    # Convert raw json data to df
    data_list = json_data['result']
    # Convert value to actual value and convert time stamp
    for d in data_list:
        d['value'] = float(d['value'])/10**6
        d['timeStamp'] = datetime.fromtimestamp(int(d['timeStamp'])).strftime('%Y-%m-%dT%H:%M:%S')
    df = pd.DataFrame(data_list)
    return df

def write_token_data(data):
    # Write df to CSV file
    output_path = './output/real-time-ERC-20.csv'

    # Get fields
    fieldnames = ['blockNumber', 'timeStamp', 'hash', 'from', 'to', 'contractAddress', 'value', 'gas', 'gasPrice', 'cumulativeGasUsed', 'tokenName']
    df = transform_token_data(data)[fieldnames]

    with open(output_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row if the file is empty
        if csv_file.tell() == 0:
            writer.writerow(fieldnames)

        # Write each row of the selected DataFrame to the file
        for row in df.values:
            writer.writerow(row)
