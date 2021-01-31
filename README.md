# P2_Kaggle_API

![portada](https://media-exp1.licdn.com/dms/image/C4D16AQECGlEQCdDeng/profile-displaybackgroundimage-shrink_200_800/0/1599817898266?e=1617840000&v=beta&t=HY3YqXDBEsd6Ee9qapnTpC4_M5mBqrJQbwvWtwg0-fg)

## Used libraries
Meter los links a las librerias

`from pygbif import occurrences as occ`

`from pygbif import species`

`import requests`

`import pandas as pd`


## Climatic Data from Kaggle
To obtain temperature data I used dataset downloaded from kaggle based on the temperature of major cities of the world named [DailyTemperatureMajorCities](https://www.kaggle.com/sudalairajkumar/daily-temperature-of-major-cities). 

## Occurrence data from GBIF
The GBIF API is a RESTful JSON based API. The base URL for v1 you should use is: https://api.gbif.org/v1/.

The main API sections are:

- **Registry**: Provides means to create, edit, update and search for information about the datasets, organizations (e.g. data publishers), networks and the means to access them (technical endpoints). 
- **Species**: Provides services to discover and access information about species and higher taxa.
- **Occurrence:** Provides access to occurrence information crawled and indexed by GBIF. 
- **Maps**: Provides simple services to show the maps of GBIF mobilized content on other sites.

The GBIF API has a spcific library in python [pygbif](https://pygbif.readthedocs.io/_/downloads/en/latest/pdf/) which allows to download data from the Global Biodiversity Information Facility [GBIF](https://www.gbif.org/es/) using different search/filter criteria.It is split up into modules for each of the major groups of API methods.
