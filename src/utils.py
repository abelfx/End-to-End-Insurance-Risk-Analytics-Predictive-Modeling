import pandas as pd

def load_data(file_path):
    """
    Loads data from a text file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path, sep='|', encoding='utf-8')
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def clean_data(df):
    """
    Performs basic data cleaning on the DataFrame.
    """
    # Example cleaning steps:
    # Convert date columns to datetime objects
    for col in df.columns:
        if 'date' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except Exception:
                pass # Ignore columns that can't be converted
    
    # Handle missing values (example: fill with median for numeric)
    for col in df.select_dtypes(include=['number']).columns:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].median(), inplace=True)
            
    return df

def get_summary_statistics(df):
    """
    Returns descriptive statistics for the DataFrame.
    """
    return df.describe(include='all')
