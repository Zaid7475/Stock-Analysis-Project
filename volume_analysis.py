import pandas as pd

def volume_analysis(df):

    print("====================")
    print("\n Volume Analysis")
    print("\n===================")

    df["Volume"] = pd.to_numeric(df["Volume"] , errors = "coerce")

    print("\n1. Highest Trading Volume:")
    print(df["Volume"].max())

    print("\n2. Lowest Trading Volume:")
    print(df["Volume"].min())

    print("\n3. Average Trading Volume:")
    print(df["Volume"].mean())

    print("\n4. Total Trading Volume:")
    print(df["Volume"].sum())

    print("\n5. Median Trading Volume:")
    print(df["Volume"].median())

    print("\n6. Highest Volume Day:")
    print(df["Volume"].idxmax())

    print("\n7. Lowest Volume Day:")
    print(df["Volume"].idxmin())

    average_volume = df["Volume"].mean()

    print("\n8. Days with Above Average Volume:")
    print((df["Volume"] > average_volume).sum())

    print("\n9. Days with Below Average Volume:")
    print((df["Volume"] < average_volume).sum())

    print("\n10. Volume Analysis Summmary:")
    print("Total Records:" , df["Volume"].count())
    print("Average Volume:" , average_volume)




