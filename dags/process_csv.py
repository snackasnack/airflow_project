import pandas as pd

def process_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Split the 'name' field into 'first_name' and 'last_name'
    name_split = df['name'].str.split(' ', expand=True)
    df['first_name'] = name_split[0]
    df['last_name'] = name_split[1]
    
    # Remove zeros prepended to the 'price' field
    df['price'] = df['price'].astype(str).str.strip()
    
    # Handle empty strings and non-numeric values
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df.fillna({'price': 0}, inplace=True)
    
    # Delete any rows which do not have a name
    df = df.dropna(subset=['name'])
    
    # Create a new field 'above_100' which is True if the price is greater than 100
    df['above_100'] = df['price'] > 100
    
    # Drop the original 'name' column
    df = df.drop(columns=['name'])
    
    return df

def save_csv(df, output_path):
    # Save the processed DataFrame to a new CSV file
    df.to_csv(output_path, index=False)
    print(df)
    print(output_path)