import pandas as pd

def monthly_analysis(df):

    df["Date"] = pd.to_datetime(df["Date"])

    for col in ["Open" , "High" , "Low" , "Close" , "Volume"]:

        df[col] = pd.to_numeric(df[col] , errors = "coerce")

    df = df.dropna(subset = ["Date" , "Close"])

    df = df.sort_values("Date")

    monthly = df.set_index("Date").resample("ME").agg({
        "Open": "first" ,
        "High": "max" ,
        "Low": "min" ,
        "Close": "last" ,
        "Volume": "sum"
    })

    monthly["Monthly Return (%)"] = monthly["Close"].pct_change() * 100

    print("\n===== MONTHLY STOCK ANALYSIS =====")

    print(monthly)

    print("\nAverage Monthly Close:" , monthly["Close"].mean())

    print("Highest Monthly Close:" , monthly["Close"].max())

    print("Lowest Monthly Close:" , monthly["Close"].min())

    print("Average Monthly Volume:" , monthly["Volume"].mean())
    
    print("Average Monthly Return:" , monthly["Monthly Return (%)"].mean())

    return monthly
