import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

# URL
url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"

# Log function
def log_progress(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("code_log.txt", "a") as f:
        f.write(timestamp + " : " + message + "\n")

# Extract
def extract(url):
    log_progress("Starting data extraction")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    tables = soup.find_all('table')
    df = pd.read_html(str(tables[0]))[0]
    
    df = df[["Name", "Market cap (US$ billion)"]]
    df.rename(columns={"Market cap (US$ billion)": "MC_USD_Billion"}, inplace=True)
    
    log_progress("Data extraction complete")
    return df

# Transform
def transform(df):
    log_progress("Starting data transformation")
    
    exchange_rate = pd.read_csv("exchange_rate.csv")
    exchange_rate.set_index("Currency", inplace=True)
    
    df["MC_GBP_Billion"] = df["MC_USD_Billion"] * exchange_rate.loc["GBP"].values[0]
    df["MC_EUR_Billion"] = df["MC_USD_Billion"] * exchange_rate.loc["EUR"].values[0]
    df["MC_INR_Billion"] = df["MC_USD_Billion"] * exchange_rate.loc["INR"].values[0]
    
    df = df.round(2)
    
    log_progress("Data transformation complete")
    return df

# Load to CSV
def load_to_csv(df, path):
    log_progress("Saving data to CSV")
    df.to_csv(path, index=False)
    log_progress("Data saved to CSV")

# Load to DB
def load_to_db(df, conn, table_name):
    log_progress("Loading data to database")
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    log_progress("Data loaded to database")

# Run query
def run_query(query, conn):
    log_progress("Executing query")
    print(pd.read_sql(query, conn))
    log_progress("Query executed")

# Main execution
log_progress("ETL Job started")

df = extract(url)

df = transform(df)

load_to_csv(df, "Largest_banks_data.csv")

conn = sqlite3.connect("Banks.db")
load_to_db(df, conn, "Largest_banks")

run_query("SELECT * FROM Largest_banks LIMIT 5", conn)

conn.close()

log_progress("ETL Job finished")
``
