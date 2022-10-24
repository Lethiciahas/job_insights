import csv
from src.jobs import read


def get_unique_job_types(path):
    with open(path) as file:
        csvreader = csv.DictReader(file, delimiter=",", quotechar='"')
        list_jobs_types = set()
        for row in csvreader:
            job_types = row["job_type"]
            list_jobs_types.add(job_types)
        return list_jobs_types


def filter_by_job_type(jobs, job_type):
    filter_job = []
    for job in jobs:
        job_filter = job["job_type"]
        if job_filter == job_type:
            filter_job.append(job)
    return filter_job


def get_unique_industries(path):
    path_data = read(path)
    list_unique = set()
    for data in path_data:
        unique_industry = data["industry"]
        if len(unique_industry):
            list_unique.add(unique_industry)
    return list_unique


def filter_by_industry(jobs, industry):
    filter = []
    for job in jobs:
        industry_filter = job["industry"]
        if industry_filter == industry:
            filter.append(job)
    return filter


def get_max_salary(path):
    path_data = read(path)
    list_max_salary = []
    for salary in path_data:
        max_salary = salary["max_salary"]
        if max_salary.isnumeric():
            list_max_salary.append(int(max_salary))
    return max(list_max_salary)


def get_min_salary(path):
    path_data = read(path)
    list_min_salary = []
    for salary in path_data:
        min_salary = salary["min_salary"]
        if min_salary.isnumeric():
            list_min_salary.append(int(min_salary))
    return min(list_min_salary)


def matches_salary_range(job, salary):
    min_salary = job.get("min_salary")
    max_salary = job.get("max_salary")
    if (type(min_salary) or type(max_salary)) != int:
        raise ValueError
    if min_salary > max_salary:
        raise ValueError
    if type(salary) != int:
        raise ValueError
    return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):
    filter = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter.append(job)
        except ValueError:
            pass
    return filter
