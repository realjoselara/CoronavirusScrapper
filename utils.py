from scrapper import collect_country_from_table

def filter_countries(countries_list):
    ''' Filters the list of countries to a new list '''
    if not isinstance(countries_list, list):
        raise TypeError

    if not isinstance(countries_list[0], object):
        raise TypeError('attribute must be a list of countries objects')
    pass