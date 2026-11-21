import pandas as pd 

def trend_analysis(df):

    df["Date"] = pd.to_datetime(df["Date"] , errors = "coerce")
    df["Close"] = pd.to_numeric(df["Close"] , errors = "coerce")

    df = df.dropna(subset = ["Date" , "Close"]).sort_values("Date")

    print("=============Trend Analysis================")

    first = df["Close"].iloc[0]
    last = df["Close"].iloc[-1]

    if last > first:

        print("1. Overall Trend: Upwards")

    elif last < first:

        print("1. Overall Trend: Downwards")

    else:

        print("1. Overall Trend: Stable")

    print("2. Starting Price:" , first)

    print("3. Latest Price:" , last)

    print("4. Price Difference:" , last - first)

    print("5. Percentage Change:" ,
          ((last - first) / first) * 100 if first != 0 else "N/A")

    print("6. Highest Price:" , df["Close"].max())

    print("7. Lowest Price:" , df["Close"].min())

    print("8. Moving Average:")
    print(df["Close"].rolling(5).mean())

    change = df["Close"].diff()
    
    print("9. Up Days:" , (change > 0).sum())
    print("   Down Days:" , (change < 0).sum())

    print("10. Total Trading Days:" , len(df))
    print("    Average Price:" , df["Close"].mean())
    

