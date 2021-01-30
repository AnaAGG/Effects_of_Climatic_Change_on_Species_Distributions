import pygbif

def get_species_name_from_codes (sp):
    keys = [species.name_backbone(x)['usageKey'] for x in splist ]
    species_codes = dict(zip(splist, keys))
    return species_codes 

def get_occurences(cod_sp):
    
    years = range(1990, 2020)
    x = []
    
    for y in years:
        data = occ.search(taxonKey = cod_sp, limit = 300, country = 'ES', year = str(y))
        #Get the number of occurrences:
        x.append({str(y): data['count']})
    
        #Get the taxonomic information
        taxonomic = data["results"]
        for dictionary in taxonomic:
            species = dictionary["scientificName"]
            kingdom = dictionary["kingdom"]            
            year = dictionary["year"]           
            country = dictionary["country"]
            
        
    
        sspecies_info = {'species': species,
                       'kingdom': kingdom,
                       'country': country,
                       'year' : year
                      }
       
    
    return x, species_info 