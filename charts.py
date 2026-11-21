import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def stock_charts(df):

    df = df.copy()

    df["Date"] = pd.to_datetime(df["Date"] , errors = "coerce")

    columns = ["Open" , "Close" , "High" , "Low" , "Volume"]

    for col in columns:

        df[col] = pd.to_numeric(df[col] , errors = "coerce")

    df = df.dropna(subset=["Date" , "Open" , "High" , "Low" , "Close" , "Volume"])

    df = df.sort_values("Date")

    if df.empty:

        print("No valid stock data available!")
        return

    df["20 Day MA"] = df["Close"].rolling(20).mean()
    df["20 Day MA"] = df["Close"].rolling(20).mean()

    df["Daily Return"] = df["Close"].pct_change() * 100

    sns.set_theme(style = "whitegrid")
    plt.figure(figsize = (10,5))
    sns.lineplot(data = df , x = "Date" , y = "Close")
    plt.title("Stock Closing Price")
    plt.show()

    plt.figure(figsize = (10 , 5))
    sns.lineplot(data = df , x = "Date" , y = "Open" , label = "Open")
    sns.lineplot(data = df , x = "Date" , y = "Close" , label = "Close")
    plt.title("Opening vs Closing Price")
    plt.show()

    plt.figure(figsize = (10 , 5))
    sns.lineplot(data = df , x = "Date" , y = "High" , label = "High")
    sns.lineplot(data = df , x = "Date" , y = "Low" , label = "Low")
    plt.title("Highest vs Lowest Price")
    plt.show()

    plt.figure(figsize = (10 , 5))
    sns.barplot(data = df , x = "Date" , y = "Volume")
    plt.title("Stock Trading Volume")
    plt.xticks(rotation = 45)
    plt.show()

    df["20 Day MA"] = df["Close"].rolling(window = 20).mean()
    df["50 Day MA"] = df["Close"].rolling(window = 50).mean()


    plt.figure(figsize = (10 , 5))
    sns.lineplot(data = df , x = "Date" , y = "Close" , label = "Close")
    sns.lineplot(data = df , x = "Date" , y = "20 Day MA" , label = "20 Day MA")
    sns.lineplot(data = df , x = "Date" , y = "50 Day MA" , label = "50 Day MA")
    plt.title("Stock Moving Averages")
    plt.show()

    plt.figure(figsize = (10 , 5))
    sns.lineplot(data = df , x = "Date" , y = "Daily Return")
    plt.axhline(y = 0 , linestyle = "--")
    plt.title("Daily Stock Returns")
    plt.show()

    monthly = df.set_index("Date")["Close"].resample("ME").last()
    monthly = monthly.dropna().reset_index()

    plt.figure(figsize = (10 , 5))
    sns.lineplot(data = monthly , x = "Date" , y = "Close" , marker = "o")
    plt.title("Monthly Closing Price")
    plt.show()  

    yearly = df.groupby(df["Date"].dt.year)["Close"].last()
    yearly = yearly.reset_index()
    yearly.columns = ["Year" , "Close"]

    plt.figure(figsize = (10 , 5))
    sns.barplot(data = yearly , x = "Year" , y = "Close")
    plt.title("Yearly Closing Price")
    plt.show()

    print("All Stock Charts Generated Successfully!")
  
    


