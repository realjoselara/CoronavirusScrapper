# CoronavirusScrapper
This scrapper collects the data per country clean it and stores it to mongoDB. 

# Scrapper
Collects data from [World Meters](https://www.worldometers.info/coronavirus/) stores it in a MongoDB. Assuming a mongo db is running in your localhost.

Some assumetions:
> MongoDB is install in system as local host.

You can install the virtual enviroment using Pipenv at the top level folder. 

Install virtual Environment:
```
- pipenv shell: activates virtual environment.
- pipenv install (if you don't have pipenv install you can install it using pip -m install pipenv)
```
###Run as CLI:
If you would like to use the program a CLI (Command Line Interface), you can run as:
```
- run python covid.py -h (returns helper function on how to use the program)
```