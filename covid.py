import argparse
from scrapper import *

def options():
    '''User options for arguments'''

    parser = argparse.ArgumentParser(description="Returns and collects the data from World Meters website")
    parser.add_argument('--filter', help='show a subset of books, looks for the argument as a substring of any of the fields')
    parser.add_argument('--year', help='sort the books by year, ascending instead of default sort', action="store_true")
    parser.add_argument('--reverse', help='reverse sort', action="store_true")
    
    args = parser.parse_args()
    return args

def main():
    '''Main Pogram'''

    user_options = options()
    book_list = get_data()

    # if user_options.filter:
    #     book_list = filter_book_list(book_list, user_options.filter)
    # if user_options.year:
    #     book_list = sort_book_by_year(book_list)
    # if user_options.reverse:
    #     book_list = reverse_book_list(book_list)

    if len(book_list) > 0:
        for item in book_list:
            print(str(item))
        print("\n")
    else:
        print("Nothing was found, please try again ")


if __name__ == '__main__':
    main()