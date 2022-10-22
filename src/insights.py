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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
