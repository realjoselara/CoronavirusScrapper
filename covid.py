import argparse
from scrapper import *
import pprint

def options():
    '''User options for arguments'''

    parser = argparse.ArgumentParser(description="Collects and returns Corona Virus (COVID-19) information from World Meters website")
    parser.add_argument('--all', help='prints all current data about total infectation, death, recovered, plus individual countries information', action="store_true")
    parser.add_argument('--countries', help='prints all individual countries information about their outbreak', action="store_true")
    # parser.add_argument('--filter', help='filter flag to countries list.')
    
    args = parser.parse_args()
    return args

def main():
    '''Main Pogram'''

    user_options = options()
    covid_data = get_data()

    if user_options.all:
        covid_data = get_data() 
    if user_options.countries:
        covid_data = collect_country_from_table()

    if len(covid_data) > 0:
        pprint.pprint(covid_data)
        print("\n")
    else:
        print("Nothing was found, please try again ")


if __name__ == '__main__':
    main()