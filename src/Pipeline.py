def cleaning_dataset():
    import pandas as pd
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded csv
    '''
    
    #Gets the name of the dataset.zip
    dire = input("Introduce la direccion local: ")

    df = pd.read_csv(dire, encoding = "ISO-8859-1", sep=';')

    #Convert given row to column header for Pandas DataFrame and readjust the iloc of the rows
    headers = df.iloc[1] 
    df = pd.DataFrame(df.values[1:], columns=headers)
    df.columns = df.iloc[0,:]
    
    #Rename one column
    df2 = df.rename({'city_ascii': 'date'}, axis=1)

    #Drop some rows
    df3 = df2.drop(df2.index[0:11], axis = 0)
    
    #Given a column with a Date column in string format, convert to datatime object and extract the month and year
    df3['date'] = pd.to_datetime(df3['date'], format='%d/%m/%Y')
    df3['Year'] = pd.DatetimeIndex(df3['date']).year
    df3['Month'] = pd.DatetimeIndex(df3['date']).month
    
    df_spain = df3[['Year', 'Month', 'Madrid', 'Barcelona', 'Malaga', 'Sevilla', 'Zaragoza', 'Valencia','Bilbao']]

    return df_spain