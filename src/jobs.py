import csv

from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        csvreader = csv.DictReader(file, delimiter=",", quotechar='"')
        list_jobs = []
        for row in csvreader:
            list_jobs.append(row)
    return list_jobs
