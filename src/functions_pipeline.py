import pandas as pd

def get_header(df, iloc):
    '''
    Convert given row to column header for Pandas DataFrame and readjust the iloc of the rows
    
    Args:
        data(pd.DataFrame): working dataframe
        iloc(int): the iloc of the column we want to make heading
        
    Return:
        pd.DataFrame with the new heading determined and the ilocs readjusted
    '''
    headers = df.iloc[iloc] 
    df = pd.DataFrame(df.values[1:], columns=headers)
    df.columns = df.iloc[0, :]
    return df

def remove_rows(df):
    '''
    Remove unnecessary rows
    Args:
        df(pd.DataFrame): working dataframe
        
    Returns
        DataFrame without the eliminated rows
    '''
   
    return df.drop(df.index[0:11], axis = 0)   

def rename_columns (df, old_col, new_col):
    '''
    Rename one column
    Args:
        old_col(str): the name of the column that we want to change
        new_col(str): the new name for the column
    Returns
        DataFrame the columns changed
    '''
    
    return df.rename({old_col: new_col}, axis=1)


def get_month_year(df, col):
    '''
    Given a column with a Date column in string format, convert to datatime object and extract the month and year
    
    Args:
        df (panda DataFrame): working DataFrame
        col : the Date column in string format
        
    Returns:
        Dataframe with two new columns (Year and Month) and a Date columns in datatime format
    '''
    df[col] = pd.to_datetime(df[col], format='%d/%m/%Y')
    df['Year'] = pd.DatetimeIndex(df[col]).year
    df['Month'] = pd.DatetimeIndex(df[col]).month
    
    return df

def mean_year(df, year):
    '''
    Calculate the mean temperature by year and location
    Args:
        df(pd.DataFrame): working dataframe
        year(column of dataframe): the year column
        
    Returns
        DataFrame with the mean temperature for each location and year
    '''
    df_mean_year = df.groupby([year]).mean()
    return df_mean_year

def mean_month(df, month):
    '''
    Calculate the mean temperature by month and location
    Args:
        df(pd.DataFrame): working dataframe
        year(column of dataframe): the month column
        
    Returns
        DataFrame with the mean temperature for each location and month
    '''
    df_mean_month = df.groupby([month]).mean()
    return df_mean_month