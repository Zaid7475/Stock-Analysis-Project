import pandas as pd

def price_analysis(df):

    print("====================")
    print("\n Price Analysis")
    print("\n===================")

    price_columns = ["Open" , "High" , "Low" , "Close" , "Volume"]

    for column in price_columns:

        df[column] = pd.to_numeric(df[column] , errors = "coerce")

    print("\n1. Highest Opening Price:")
    print(df["Open"].max())

    print("\n2. Lowest Opening Price:")
    print(df["Open"].min())

    print("\n3. Highest Closing Price:")
    print(df["Close"].max())

    print("\n4. Lowest Closing Price:")
    print(df["Close"].min())

    print("\n5. Average Closing Price:")
    print(df["Close"].mean())

    df["Price Change"] = df["Close"] - df["Open"]

    print("\n6. Daily Price Change:")
    print(df["Price Change"])

    df["Percentage Change"] = ((df["Close"] - df["Open"]) / df["Open"]) * 100

    print("\n7. Percentage Change:")
    print(df["Percentage Change"])

    print("\n8. Highest Daily Gain:")
    print(df["Price Change"].max())

    print("\n9. Highest Daily Loss:")
    print(df["Price Change"].min())

    print("\n10. Overall Price Range:")
    print(df["High"].max() - df["Low"].min())




