from pygbif import occurrences as occ
from pygbif import species
import requests
import pandas as pd

def get_species_name_from_codes (splist):
    keys = [species.name_backbone(x)['usageKey'] for x in splist ]
    species_codes = dict(zip(splist, keys))
    return species_codes   

def get_occurences(sp):
    
    years = range(1970, 2020)
    x = []
    
    for y in years:
        data = occ.search(taxonKey = sp, limit = 300, country = 'ES', year = str(y))
        #Get the number of occurrences:
        x.append({str(y): data['count']})
        
        # Set all the data in an unique dictionary
        final = {}
        for d in x:
            for k in d.keys():
                final[k] = final.get(k,0) + d[k]
       
    return final

def get_taxonomic_info(sp):
    data = occ.search(taxonKey = sp, limit = 300, country = 'ES', year = '2016')
    taxonomic = data["results"] 
    for dictionary in taxonomic:
        Species = dictionary["scientificName"]
        kingdom = dictionary["kingdom"] 
        genus = dictionary['genus']
        family = dictionary['family']           
        country = dictionary["country"]
        records = dictionary['basisOfRecord']
        pub = dictionary['publishingCountry']
            
        
    
    species_info = {'species': Species,
                    'kingdom': kingdom,
                    'Genus': genus, 
                    'Family': family,
                    'country': country,
                    'records': records,
                    'Publishing_country': pub
               }
    return species_info

def join_occurrences_taxonomic(sp):
    '''
    Receive taxonomic information dictionary and dictictionry with occurences/year
    
    Args:
    
    
    Returns
        jsdf
    '''
    # occurrence dictionary to dataframe
    df_occurrences = pd.DataFrame.from_dict(data = get_occurences(sp),  orient='index').reset_index()
    df_occurrences.columns = ['Year','Occurrences']
    
    #taxonomic dictionary to dataframe
    df_taxonomic = pd.DataFrame(data = get_taxonomic_info(sp), index = [0])
    df_taxonomic = pd.concat([df_taxonomic]*50, ignore_index=True)
    
    # concatenate occurences with taxonomic information
    sp1 = pd.concat([df_occurrences,df_taxonomic], axis=1)
    
    
    return sp1