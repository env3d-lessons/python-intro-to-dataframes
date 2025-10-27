#!/home/codespace/.python/current/bin/python

import pandas
import json
import pprint
import csv
import sys

csv_file= sys.argv[1]
def to_json():
    df = pandas.read_csv(csv_file)
    json_df=df.to_json(orient='records', lines=True)
    return json_df


if __name__ == "__main__":   
   print((to_json()))