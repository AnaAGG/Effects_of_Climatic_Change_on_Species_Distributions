# P2_Kaggle_API

![portada](https://media-exp1.licdn.com/dms/image/C4D16AQECGlEQCdDeng/profile-displaybackgroundimage-shrink_200_800/0/1599817898266?e=1617840000&v=beta&t=HY3YqXDBEsd6Ee9qapnTpC4_M5mBqrJQbwvWtwg0-fg)

## Objective and hypothesis
        The objetive of this proyect is learn to combine multiple tools to get data, from a dataset and APIs. I also 
        
        Main hypothesis, the increase in temeparture has lead to reduce the occurrence of ndemic species, while warm tolerant species have increase their occurrence in the last years. 

    

## Climatic Data from Kaggle
To obtain temperature data I used dataset downloaded from kaggle based on the temperature of major cities of the world named [TemperatureHistoryof1000Cities1989to2020](https://www.kaggle.com/hansukyang/temperature-history-of-1000-cities-1980-to-2020). 


## Occurrence data from GBIF
The GBIF API is a RESTful JSON based API. The base URL for v1 you should use is: https://api.gbif.org/v1/.

The main API sections are:

- **Registry**: Provides means to create, edit, update and search for information about the datasets, organizations (e.g. data publishers), networks and the means to access them (technical endpoints). 
- **Species**: Provides services to discover and access information about species and higher taxa.
- **Occurrence:** Provides access to occurrence information crawled and indexed by GBIF. 
- **Maps**: Provides simple services to show the maps of GBIF mobilized content on other sites.

The GBIF API has a spcific library in python [pygbif](https://pygbif.readthedocs.io/_/downloads/en/latest/pdf/) which allows to download data from the Global Biodiversity Information Facility [GBIF](https://www.gbif.org/es/) using different filter criteria. It is split up into modules for each of the major groups of API methods.

## Data cleaning

- 1. Data from kaggle was cleaned used a pipeline..
- 2. Data from GBIF API was downloaded for XXX species including birds, trees, herbaceous. All the species informaation was obtained through two vias:
     - **Taxonomic** information from selected species
     - **Occurrence** data from the studied years.



|        |   |Studied species   |   |   |
|:-----:|:-:|:---:|:---:|:---:|
| Apus affinis  | fsdfdsf  |  Abies pinsapo |   |Parnasius_apollo   |
| Sonchus tenerrimus | Lanius minor  |Araujia sericiferas|   | Ciconia ciconia  |  Abies pinsapo | |   |   |  Abies pinsapo | ugugo  |Parnasius apollo   |
  |   |
   |   |   |
|   |   |   |   |   |


 



## Libraries

[from pygbif import occurrences as occ](https://pypi.org/project/pygbif/)

[from pygbif import species](https://pypi.org/project/pygbif/)

[import requests](https://pypi.org/project/requests/2.7.0/)

[import pandas as pd](https://pandas.pydata.org/)
