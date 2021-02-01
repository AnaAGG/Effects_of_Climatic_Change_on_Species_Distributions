# P2_Kaggle_API

![portada](https://media-exp1.licdn.com/dms/image/C4D16AQECGlEQCdDeng/profile-displaybackgroundimage-shrink_200_800/0/1599817898266?e=1617840000&v=beta&t=HY3YqXDBEsd6Ee9qapnTpC4_M5mBqrJQbwvWtwg0-fg)

## Objective and hypothesis
**Objetive**

Learn to combine multiple tools to get data, from a dataset and APIs. 
        
**Hypothesis:** 

The increase in temperature has lead to reduce the occurrence of endemic species. On the other hand, exotic species, which are more heat tolerant, are being favoured by the rising temperatures of the last decades.

    

## Climatic Data from Kaggle
To obtain temperature data I used dataset downloaded from kaggle based on the temperature of major cities of the world, [TemperatureHistoryof1000Cities1989to2020](https://www.kaggle.com/hansukyang/temperature-history-of-1000-cities-1980-to-2020). 


This database represents temperature time-series value in degrees Celsius, for 1000 most populous cities in the world, from January 1980 to September 2020. We start from a dataset with 14896 rows and 1001 columns. Rows represent the different records for each day of the years studied. Columns represent each of the cities for which there are records.

At the end of the cleaning process the dataset we remove 12 rows and **added two columns to the month and year information**. Finnaly, I have generated two different databases that I will use to relate the information on species occurrences and temperatures:

- Mean temperature by year and location
- Mean temperature by month and location


## Occurrence data from GBIF
The GBIF API is a RESTful JSON based API. The base URL for v1 you should use is: https://api.gbif.org/v1/.

The main API sections are:

- **Registry**: Provides means to create, edit, update and search for information about the datasets, organizations (e.g. data publishers), networks and the means to access them (technical endpoints). 
- **Species**: Provides services to discover and access information about species and higher taxa.
- **Occurrence:** Provides access to occurrence information crawled and indexed by GBIF. 
- **Maps**: Provides simple services to show the maps of GBIF mobilized content on other sites.

The GBIF API has a spcific library in python [pygbif](https://pygbif.readthedocs.io/_/downloads/en/latest/pdf/) which allows to download data from the Global Biodiversity Information Facility [GBIF](https://www.gbif.org/es/) using different filter criteria. It is split up into modules for each of the major groups of API methods.

## Data cleaning

- 1. Data from kaggle: for the temperature database cleaning I used a pipeline generating a stream of cleanup functions that transformed the database for use.
- 2. Data from GBIF API was downloaded for XXX species including birds, trees, herbaceous. All the species informaation was obtained through two vias:
     - **Taxonomic** information from selected species
     - **Occurrence** data from the studied years.



|        |   |Included species   |   |   |
|:-----:|:-:|:---:|:---:|:---:|
|  *Abies pinsapo*  | *Anas penelope*  | *Apus affinis*  | *Araujia sericiferas* |*Carpobrotus edulis* |||*Ciconia ciconia*|*Cortaderia selloana*|   ||  |   ||  |   |  | 
  | *Calotriton arnoldi*  |*Grus grus*|  *Lanius minor* |  Parnasius apollo* |*Silene ciliata* |
  | *Sonchus tenerrimus* |  *Vanellus vanellus* |  |  | 
  |   |   |   |   |


 ## Main results

In general, in both plants and birds, the results obtained in this approach show that species with warmer affinities have increased their occurrences in recent years. On the other hand, those native species not adapted to rising temperatures have decreased their occurrence. 


## Libraries

[from pygbif import occurrences as occ](https://pypi.org/project/pygbif/)

[from pygbif import species](https://pypi.org/project/pygbif/)

[import requests](https://pypi.org/project/requests/2.7.0/)

[import pandas as pd](https://pandas.pydata.org/)

[import numpy as np](https://numpy.org/doc/)

[import matplotlib.pyplot as plt](https://matplotlib.org/3.1.1/contents.html)

[import seaborn as sns](https://seaborn.pydata.org/)
