import argparse
import logging
import json
import csv
from datetime import datetime
from pytz import timezone
from dateutil import parser as dateparser
import pytz

def main():
  parser = argparse.ArgumentParser(description='Args Parser')
  parser.add_argument('--json', type=str, required=True)
  args = parser.parse_args()

  json_file = args.json

  with open(json_file, 'r', encoding='utf-8') as jfile:
    json_data = json.load(jfile)

  extractedJson = []
  
  for item in json_data['imdata']:
    try:
      extractedJson.append([
        item['l1PhysIf']['attributes']['dn'],
        # item['l1PhysIf']['attributes']['sample'],
        item['l1PhysIf']['attributes']['descr'],
        item['l1PhysIf']['attributes']['speed'],
        item['l1PhysIf']['attributes']['mtu'],
        item['l1PhysIf']['attributes']['modTs']
      ])
    except:
      logging.error("KeyError: Key doesn't exist")
      break

  # Sorting by DN in descending order
  extractedJson.sort(reverse = True)

  # Change UTC time to PST
  for item in extractedJson:
    date = dateparser.parse(item[4])
    item[4] = date.astimezone(timezone('Asia/Manila'))

  csv_file = "csvfile.csv"
  csvfields = ['DN','DESCRIPTION','SPEED','MTU','MODIFICATION_TIMESTAMP']

  with open(csv_file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(csvfields)
    csvwriter.writerows(extractedJson)
  


if __name__=="__main__":
  main()