from bs4 import BeautifulSoup as bs
from heapq import nlargest
from re import sub
from urllib.request import urlopen, HTTPError

"""
This file is mainly about retrieving top 125 salaries from the salary table.
"""

# Retrieve salaries from the salary table and do error handlings
def retrieve_stats(url):
    try: 
        html = urlopen(url)
        soup = bs(html, features="lxml")
        elems = soup.findAll('td', {"class": "player-salary"})

        salaries = []
        for e in elems:
            salary = e.text
            
            if not _has_numbers(salary):
                continue

            salary = sub(r'[^0-9\.]', '', salary)
            salaries.append(int(salary))
        return salaries

    except HTTPError as e:
        if e.code == 404:
            print("Page Not Found")
        elif e.code == 403:
            print("Access Denied")
        else:
            print(e.reason)

    except AttributeError as e:
        print("Cannot successfully scrap values from the player-salary tag")

# Get the top 125 salaries from the list
def get_largest_125_salaries(salaries):
    top_largest_salaries = nlargest(125, salaries)
    return top_largest_salaries

# Check if an input string has any digit or no
def _has_numbers(input_string):
    return any(char.isdigit() for char in input_string)
