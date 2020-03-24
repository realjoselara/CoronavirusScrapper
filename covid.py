import argparse
from scrapper import *
import pprint

def options():
    '''User options for arguments'''

    parser = argparse.ArgumentParser(description="Returns and collects the data from World Meters website")
    parser.add_argument('--all', help='prints all current data about total infectation, death, recovered, plus individual countries information', action="store_true")
    # parser.add_argument('--filter', help='show a subset of data, looks for the argument as a substring of any of the fields')
    # parser.add_argument('--reverse', help='reverse sort', action="store_true")
    
    args = parser.parse_args()
    return args

def main():
    '''Main Pogram'''

    user_options = options()
    covid_data = get_data()

    if user_options.all:
        covid_data = get_data() 

    if len(covid_data) > 0:
        pprint.pprint(covid_data)
        print("\n")
    else:
        print("Nothing was found, please try again ")


if __name__ == '__main__':
    main()