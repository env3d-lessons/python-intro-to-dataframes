# Question 1

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

Write your solution into a file named *`taxi.py`*.

# Question 2

The file `reddit.jl` contains an extraction of the reddit frontpage data in the
“Json Line” format, where each line is a separate json object.

Write a python script called *`reddit.py`* that will process and extract the
"subreddit”, "title”, and "score” fields from the reddit.jl file and write those
fields to stdout in csv format.  

There are many ways to achieve this.  You may want to review the 
(working with json)[https://www.linkedin.com/learning/data-ingestion-with-python/working-with-json]
video.  You can also explore the `read_json` function from the pandas library.

# Question 3 (Challenge)

Recall from https://github.com/env3d-lessons/linux-bash-challenge that you can access any wordpress
site's JSON data using the url https://${WORDPRESS_SITE}/wp-json/wp/v2/posts/?per_page=10&context=embed 
where WORDPRESS_SITE is the domain name of any sites that runs the wordpress software.  For instance, 
https://time.com/wp-json/wp/v2/posts/?per_page=10&context=embed will give you the JSON data for
time.com.

Write a python script called *`wordpress.py`* that takes in one command-line argument that indiciates
the domain of the wordpress based site, and extracts the current title text and thumbnail url for
the top 10 current posts of that site.

See the terminal interaction below:

```
@env3d ➜ /workspaces/python-intro-to-dataframes (main) $ python wordpress.py time.com
Jimmy Carter Casts His 2024 Ballot by Mail ,https://api.time.com/wp-content/uploads/2024/10/jimmy-carter.jpg?quality=85&w=150&h=150&crop=1
The Perils of Trolling Trump on His Weird Dance Party,https://api.time.com/wp-content/uploads/2024/10/GettyImages-2177752701.jpg?quality=85&w=150&h=150&crop=1
Elon Musk Commits $70 million to Boost Donald Trump,https://api.time.com/wp-content/uploads/2024/10/musk.jpg?quality=85&w=150&h=150&crop=1
How Youth Climate Anxiety Became a Convenient Foil for the Right,https://api.time.com/wp-content/uploads/2024/10/Youth-climate-protest-NYC-Sept-2024.jpg?quality=85&w=150&h=150&crop=1
Why Vinegar Is So Good for You,https://api.time.com/wp-content/uploads/2024/10/HealthBenefitsofVinegar.png?w=150&h=150&crop=1
Why You Shouldn't Store Your Money in Payment Apps,https://api.time.com/wp-content/uploads/2024/10/money_09fb40.jpg?quality=85&w=150&h=150&crop=1
'American Malaria' Is on the Rise,https://api.time.com/wp-content/uploads/2024/10/ticks-us-disease.jpg?quality=85&w=150&h=150&crop=1
Why Youth Entrepreneurs Are Key To Tackling Climate Change in Africa,https://api.time.com/wp-content/uploads/2024/10/africa-youth-climate-entrepreneurs.jpg?quality=85&w=150&h=150&crop=1
The Deep Roots of Today's Self-Development Industry,https://api.time.com/wp-content/uploads/2024/09/lily-dale-statue.jpg?quality=85&w=150&h=150&crop=1
What's Behind the Widening Gender Wage Gap in the U.S.?,https://api.time.com/wp-content/uploads/2024/10/GettyImages-2085597713.jpg?quality=85&w=150&h=150&crop=1

@env3d ➜ /workspaces/python-intro-to-dataframes (main) $ python wordpress.py nasa.gov
Navigating Space and Sound: Jesse Bazley Supports Station Integration and Colleagues With Disabilities,https://www.nasa.gov/wp-content/uploads/2024/10/final-shift-rotated.jpg?w=150&h=150&crop=1
The View from Space Keeps Getting Better  ,https://www.nasa.gov/wp-content/uploads/2022/08/landsat_9_release.jpeg?w=150&h=150&crop=1
Sacrifice and Success: NASA Engineer Honors Family Roots,https://images-assets.nasa.gov/image/AFRC2023-0170-07/AFRC2023-0170-07~large.jpg?w=1920&h=1279&fit=clip&crop=faces%2Cfocalpoint
Sacrificio y Éxito: Ingeniero de la NASA honra sus orígenes familiares,https://images-assets.nasa.gov/image/AFRC2023-0170-07/AFRC2023-0170-07~large.jpg?w=1920&h=1279&fit=clip&crop=faces%2Cfocalpoint
"The Marshall Star for October 16, 2024",https://www.nasa.gov/wp-content/uploads/2024/10/54067151504-46075ee405-k.jpg?w=150&h=150&crop=1
NASA Seeks Innovative Ideas with Revamped Procurement Framework,https://www.nasa.gov/wp-content/uploads/2024/10/nasa-hq-flags.jpg?w=150&h=150&crop=1
"NASA to Embrace Commercial Sector, Fly Out Legacy Relay Fleet ",https://www.nasa.gov/wp-content/uploads/2024/10/csp.webp?w=150&h=150&crop=1
```

HINT: There are many ways to achieve the above.  You will want to review the following

 - Python's `sys` module for reading command-line arguments (https://www.geeksforgeeks.org/command-line-arguments-in-python/)
 - Python's `requests` module for reading data from URL (https://www.linkedin.com/learning/data-ingestion-with-python/making-http-calls)
 - Pandas Dataframe's to_csv() function for easy conversion to csv format (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)