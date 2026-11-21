import pandas as pd

def basic_stats(df):

    print("====================")
    print("\n Basic Statistics")
    print("\n===================")

    numeric_columns = ["Open" , "High" , "Low" , "Close" , "Volume"]

    for column in numeric_columns:

        df[column] = pd.to_numeric(df[column] , errors = "coerce")

    print("\n1. Number of Records:")
    print(len(df))

    print("\n2. Mean:")
    print(df[numeric_columns].mean())

    print("\n3. Median:")
    print(df[numeric_columns].median())

    print("\n4. Minimum:")
    print(df[numeric_columns].min())

    print("\n5. Maximum:")
    print(df[numeric_columns].max())

    print("\n6. Standard Deviation:")
    print(df[numeric_columns].std())

    print("\n7. Variance:")
    print(df[numeric_columns].var())

    print("\n8. Range:")
    print(df[numeric_columns].max() - df[numeric_columns].min())

    print("\n9. Five Number Summary:")
    print(df[numeric_columns].describe().loc[
            ["min" , "25%" ,"50%" , "75%" , "max"]
        ])




