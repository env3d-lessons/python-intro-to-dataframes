#!/home/codespace/.python/current/bin/python

import pandas
import csv
import json


def to_csv_from_json():
    file='reddit.jl'
    with open(file, 'r') as f:
        data=[json.loads(line) for line in f]
        df = pandas.DataFrame(data)

# Isolates the three columns needed for the exercise 
        df =df[['subreddit','title','score']]

# converts to csv format
        csv_file=df.to_csv()
        return csv_file
# subreddit”, "title”, and "score”
if __name__ == "__main__":   
    print(to_csv_from_json())