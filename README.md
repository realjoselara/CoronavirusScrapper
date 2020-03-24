# covid19api
Building an API that returns the current information about the Coronavirus (Covid-19), the scrapper collects the data per country clean it and stores it to mongoDB.

# Scrapper
Collects data from [World Meters](https://www.worldometers.info/coronavirus/) stores it in a MongoDB. Assuming a mongo db is running in your localhost.

Some assumetions:
> MongoDB is install in system as local host.

You can install the virtual enviroment using Pipenv at the top level folder. 

Run code as:
```
- pipenv shell: activates virtual environment.
- pipenv install (if you don't have pipenv install you can install it using pip -m install pipenv)
- run python app.py -h (returns helper function on how to use the program)
```