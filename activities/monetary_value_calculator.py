from activities.stats_retrieval import get_largest_125_salaries, retrieve_stats

"""
This file is mainly about calculate the monetary value based on at most 125 data.
"""

# If there are no largest salaries in the list, return the monetary value as None.
# Otherwise, calculate the average of highest salaries.
def get_monetary_value(url):
    salaries = retrieve_stats(url)
    top_largest_salaries = get_largest_125_salaries(salaries)

    if len(top_largest_salaries) == 0:
        monetary_value = None
    else:
        monetary_value = sum(top_largest_salaries)/len(top_largest_salaries)
    return monetary_value
