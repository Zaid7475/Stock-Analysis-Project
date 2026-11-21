import pandas as pd

def outlier_analysis(df):

    print("\n==============Outlier Analysis===============")

    columns = ["Open" , "High" , "Low" , "Close" , "Volume"]
    
    for col in columns:
    
        df[col] = pd.to_numeric(df[col] , errors = "coerce")

    Q1 = df["Close"].quantile(0.25)
    Q3 = df["Close"].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 - 1.5 * IQR

    outliers = df[(df["Close"] < lower) | (df["Close"] > upper)]

    print("1. Total Closing Price Outliers:" , len(outliers))

    print("2. Highest Outlier:" , outliers["Close"].max())

    print("3. Lowest Outlier:" , outliers["Close"].min())

    print("4. Upper Limit:" , upper)

    print("5. Lower Limit:" , lower)

    print("6. Average Closing Price:" , df["Close"].mean())

    print("7. Median Closing Price:" , df["Close"].median())

    percentage = (len(outliers) / df["Close"].count()) * 100

    print("8. Outlier Percentage:" , percentage , "%")

    print("9. Outlier Records:")
    print(outliers)

    print("10. Normal Records:" , df["Close"].count() - len(outliers))
    
    


    

