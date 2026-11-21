import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def display_data():

    api_key = os.getenv("API_KEY")

    symbol = input("Enter Any Symbol").upper()

    url = "https://www.alphavantage.co/query"

    params = {

        "function" : "TIME_SERIES_DAILY" ,
        "symbol" : symbol ,
        "outputsize" : "compact" ,
        "apikey" : api_key

    }
    

    response = requests.get(url , params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:

        print("\nUnable to get stock data.")
        print(data)
        return

    df = pd.DataFrame.from_dict(

        data["Time Series (Daily)"] ,
        orient = "index"

        )

    df.index.name = "Date"
    
    df.reset_index(inplace = True)

    df.columns = [

        "Date" ,
        "Open" ,
        "High" ,
        "Low" ,
        "Close" ,
        "Volume"
        
    ]

    df = df.sort_index(ascending = False)

    print("\n======Stock Data=====")
    print(df)

    return df