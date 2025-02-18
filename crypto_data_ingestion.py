# !/usr/bin/env python3
import pandas as pd
import requests
import json
from datetime import datetime
import configparser
from elasticsearch import Elasticsearch

print("------------------------------------------------------------------------------------")
print(f"Batch started at {datetime.now()}", end='\n')
global es


def get_connection(host='localhost', port=9200):
    global es
    es = Elasticsearch([{'scheme': 'http', 'host': host, 'port': port}])
    return es


def save_data(data, index_name='crypto_data'):
    try:
        global es
        response = es.index(index=index_name, document=data)
        return True
    except Exception as e:
        print("Exception occured while saving data into elastic : {e}")
        return False


def fetch_crypto_details():
    try:
        url = "https://api.coincap.io/v2/assets"
        headers = {
            "Authorization": "Bearer 66bc99f3-6892-4b63-a1a8-d7caa946baf5"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            if response.text is not None and len(response.text) > 0:
                print("Data fetched successfully from API")
                return (json.loads(response.text))
            raise Exception("No data available from source")
        else:
            raise Exception("Unable to communicate with api")
    except Exception as e:
        print(f"Exception occurred while fetching the data {e}")


def controller():
    try:

        if get_connection():
            print("Elastic engine is active..Proceeding further")
        else:
            raise Exception("Elastic inactive, aborting process")

        batch_details = fetch_crypto_details()
        save_data(batch_details)

        print(f"Batch successfully executed and ended at {datetime.now()}", end='\n')



    except Exception as e:
        print(e)


if __name__ == "__main__":
    controller()
