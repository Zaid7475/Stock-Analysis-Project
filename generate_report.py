import pandas as pd
from datetime import datetime


def generate_report(df , forecast=None):

    df = df.copy()

    df["Date"] = pd.to_datetime(df["Date"] , errors = "coerce")

    for col in ["Open" , "High" , "Low" , "Close" , "Volume"]:

        df[col] = pd.to_numeric(df[col] , errors = "coerce")

    df = df.dropna(subset=["Date" , "Close"])
    df = df.sort_values("Date")

    if df.empty:

        print("No valid stock data!")
        return

    total_records = len(df)
    highest = df["High"].max()
    lowest = df["Low"].min()
    average = df["Close"].mean()
    volume = df["Volume"].sum()
    avg_volume = df["Volume"].mean()

    first = df["Close"].iloc[0]
    last = df["Close"].iloc[-1]
    returns = ((last - first) / first) * 100

    monthly = df.set_index("Date").resample("ME").agg({
        "Open": "first" ,
        "High": "max" ,
        "Low": "min" ,
        "Close": "last" ,
        "Volume": "sum"
    })

    yearly = df.groupby(df["Date"].dt.year).agg({
        "Open": "first" ,
        "High": "max" ,
        "Low": "min" ,
        "Close": "last" ,
        "Volume": "sum"
    })

    report = [
        "=" * 45 ,
        "          STOCK ANALYSIS REPORT" ,
        "=" * 45 ,
        f"Generated: {datetime.now()}" ,
        f"Start Date: {df["Date"].min().date()}" ,
        f"End Date: {df["Date"].max().date()}" ,

        "\n--- DATASET OVERVIEW ---" ,
        f"Total Records: {total_records}" ,
        f"Total Volume: {volume:,.2f}" ,

        "\n--- BASIC ANALYSIS ---" ,
        f"Highest Price: {highest:.2f}" ,
        f"Lowest Price: {lowest:.2f}" ,
        f"Average Close: {average:.2f}" ,
        f"Average Volume: {avg_volume:.2f}" ,
        f"First Close: {first:.2f}" ,
        f"Latest Close: {last:.2f}" ,
        f"Overall Return: {returns:.2f}%" ,

        "\n--- MONTHLY ANALYSIS ---" ,
        monthly.round(2).to_string() ,

        "\n--- YEARLY ANALYSIS ---" ,
        yearly.round(2).to_string()
    ]

    if forecast is not None:

        report.extend([
            "\n--- STOCK PREDICTION ---" ,
            forecast.round(2).to_string(index = False)
        ])

    report.append("\n" + "=" * 45)
    report.append("             END OF REPORT")
    report.append("=" * 45)

    with open("stock_analysis_report.txt" , "w" , encoding = "utf-8") as file:
        
        file.write("\n".join(report))

    print("\nReport Generated Successfully!")
    
    print("File: stock_analysis_report.txt")

    return "stock_analysis_report.txt"
