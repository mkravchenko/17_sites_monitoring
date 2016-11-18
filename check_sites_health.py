import os
import requests
from whois import whois
from datetime import datetime
import sys
import calendar


def load_urls4check(path):
    with open(path) as f:
        data = f.readlines()
    return data


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return False


def get_domain_expiration_date(domain_name):
    domain_info = whois(domain_name)
    expiration_site_date = domain_info.expiration_date
    if type([]) == type(expiration_site_date):
        expiration_site_date = expiration_site_date[-1]
    return expiration_site_date


def is_domain_expiration_date_more_then_month(expiration_date):
    current_day = datetime.today()
    month_next = calendar.monthrange(current_day.year, current_day.month + 1)[1]
    diff = expiration_date - datetime.today()
    if month_next <= diff.days:
        return True
    return False


def run_main_operations():
    urls_list = load_urls4check(path_to_file_with_urls)
    for url in urls_list:
        url = url.replace("\n", "")
        is_status_code_200 = is_server_respond_with_200(url)
        expiration_date = get_domain_expiration_date(url)
        is_expiration_date_more_then_month = is_domain_expiration_date_more_then_month(expiration_date)
        print_site_info(url, is_status_code_200, is_expiration_date_more_then_month)


def print_site_info(url, is_status_code_200, is_expiration_date_more_then_month):
    if is_status_code_200 and is_expiration_date_more_then_month:
        print("{0} - PASSED.".format(url))
    elif not is_status_code_200 and is_expiration_date_more_then_month:
        print('{} - status code FAILED.'.format(str(url)))
    elif is_status_code_200 and not is_expiration_date_more_then_month:
        print("{0} - expiration date FAILED.".format(url))
    else:
        print("{0} - status code and expiration date FAILED.".format(url))


def get_path_to_file():
    def is_path_valid(path_to_file):
        if not os.path.exists(path_to_file):
            print("Please check input path to the file with urls.")
            return False
        return True

    def enter_password():
        while True:
            path_to_file = input("Enter path to file with urls: ")
            is_valid = is_path_valid(path_to_file)
            if not path_to_file:
                exit("Program stopped.")
            if is_valid:
                return path_to_file

    if len(sys.argv) <= 1:
        path = enter_password()
    else:
        path = sys.argv[1]
        is_path_valid_file_path = is_path_valid(path)
        if not is_path_valid_file_path:
            path = enter_password()
    return path


if __name__ == '__main__':
    path_to_file_with_urls = get_path_to_file()
    run_main_operations()
