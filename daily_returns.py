import pandas as pd

def daily_returns(df):

    print("\n=============Daily Returns==============")

    df["Close"] = pd.to_numeric(df["Close"] , errors = "coerce")

    df = df.dropna(subset = ["Close"])

    df["Daily Return"] = df["Close"].pct_change() * 100

    print("1. Daily Returns:")
    print(df["Daily Return"])

    print("2. Average Daily Return:" , 
          df["Daily Return"].mean())

    print("3. Maximum Daily Return:" , 
          df["Daily Return"].max())

    print("4. Minimum Daily Return:" , 
          df["Daily Return"].min())

    print("5. Positive Returns:" ,
          (df["Daily Return"] > 0).sum())

    print("6. Negative Returns:" ,
          (df["Daily Return"] < 0).sum())

    print("7. Zero Returns:" ,
          (df["Daily Return"] == 0).sum())

    print("8. Return Standard Deviation:" ,
          df["Daily Return"].std())

    first = df["Close"].iloc[0]
    last = df["Close"].iloc[-1]

    print("9. Total Return:" ,
          ((last - first) / first) * 100 if first != 0 else "N/A")

    print("10. Total Trading Days:" ,
          df["Daily Return"].count())