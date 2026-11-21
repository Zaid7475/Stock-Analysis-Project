import pandas as pd

def yearly_analysis(df):

    df = df.copy()

    df["Date"] = pd.to_datetime(df["Date"] , errors = "coerce")

    columns = ["Open" , "High" , "Low" , "Close" , "Volume"]

    for col in columns:
         
        df[col] = pd.to_numeric(df[col] , errors = "coerce")

    df = df.dropna(subset=["Date" , "Close"])

    df = df.sort_values("Date")

    df["Year"] = df["Date"].dt.year

    yearly = df.groupby("Year").agg({
        "Open": "first" ,
        "High": "max" ,
        "Low": "min" ,
        "Close": "last" ,
        "Volume": "sum"
    })

    yearly["Yearly Return (%)"] = (
        yearly["Close"].pct_change() * 100
    )

    print("\n========== YEARLY STOCK ANALYSIS ==========")

    print(yearly.round(2))

    print("\n========== YEARLY SUMMARY ==========")

    print("Average Yearly Close:" ,
          round(yearly["Close"].mean() , 2))

    print("Highest Yearly Close:" ,
          round(yearly["Close"].max() , 2))

    print("Lowest Yearly Close:" ,
          round(yearly["Close"].min() , 2))

    print("Average Yearly Volume:" ,
          round(yearly["Volume"].mean() , 2))

    print("Average Yearly Return:" ,
          round(yearly["Yearly Return (%)"].mean() , 2) , "%")

    return yearly
