# Question 1 (70%)

Using pandas, you can read and output json very easily.  Re-do
the chapter 2 exercise
(https://www.linkedin.com/learning/data-ingestion-with-python/challenge-csv-to-json?resume=false&u=57075641)
but use the pandas dataframe.to_json() function.  Your solution will
only consist of a few lines of code!

Please note that you simply need to write a python script (or even a
python one-liner) to ingest my taxi.csv file
https://raw.githubusercontent.com/env3d/python-data-ingestion-basics/main/taxi.csv
and output json line format.

My example code is here: https://github.com/env3d/python-data-ingestion-basics/ 

Read the dataframe documentation here:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html 

For those interested, take a look at the official JSON format specification:
https://www.json.org/json-en.html 

Write your solution into a file named taxi.py.

# Question 2

The file `reddit.jl` contains an extraction of the reddit frontpage data in the
“Json Line” format, where each line is a separate json object.

Write a script (or a combination of scripts) that will process and extract the
"subreddit”, "title”, and "score” fields from the reddit.jl file and write those
fields to stdout in csv format.  

There are many different ways to achieve this, below I used 2 separate scripts,
load_reddit.sh to download and convert the reddit.jl file into proper json format
and call load_reddit.py.  

I then use load_reddit.py to ingest the json format, extract the fields, and output
to csv format.  

