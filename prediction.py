import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , mean_squared_error

def stock_prediction(df):

    df = df.copy()

    df["Date"] = pd.to_datetime(df["Date"] , errors = "coerce")
    df["Close"] = pd.to_numeric(df["Close"] , errors = "coerce")

    df = df.dropna(subset = ["Date" , "Close"])
    df = df.sort_values("Date")
    df = df.drop_duplicates(subset = "Date" , keep = "last")

    if len(df) < 25:

        print("At least 25 records are required!")
        return

    prices = df["Close"].reset_index(drop = True)

    data = pd.DataFrame({
        f"Lag_{i}": prices.shift(i)
        for i in range(1 , 6)
    })
    data["Target"] = prices
    data = data.dropna()

    split = int(len(data) * 0.80)

    X = data.drop("Target" , axis = 1)
    y = data["Target"]

    model = LinearRegression()
    
    model.fit(X.iloc[:split] , y.iloc[:split])

    predictions = model.predict(X.iloc[split:])
    actual = y.iloc[split:]

    mae = mean_absolute_error(actual , predictions)
    rmse = mean_squared_error(actual , predictions) ** 0.5

    print("\n===== MODEL EVALUATION =====")
    print("MAE:" , round(mae , 2))
    print("RMSE:" , round(rmse , 2))

    model.fit(X , y)

    history = list(prices)
    future_predictions = []

    for _ in range(7):

        features = pd.DataFrame([{
            f"Lag_{i}": history[-i]
            for i in range(1 , 6)
        }])

        value = model.predict(features)[0]

        future_predictions.append(value)
        history.append(value)

    dates = pd.bdate_range(
        start = df["Date"].iloc[-1] + pd.Timedelta(days=1) ,
        periods = 7
    )

    forecast = pd.DataFrame({
        "Date": dates ,
        "Predicted Close": future_predictions
    })

    print("\n===== NEXT 7 DAYS PREDICTION =====")

    forecast["Predicted Close"] = forecast["Predicted Close"].round(2)
    print(forecast.to_string(index = False))

    actual_data = df[["Date" , "Close"]].tail(60).copy()
    actual_data.columns = ["Date" , "Price"]
    actual_data["Type"] = "Actual"

    predicted_data = forecast.rename(
        columns = {"Predicted Close": "Price"}
    )
    predicted_data["Type"] = "Predicted"

    chart = pd.concat([actual_data , predicted_data])

    sns.set_theme(style = "whitegrid")
    plt.figure(figsize = (12 , 6))

    sns.lineplot(
        data = chart ,
        x = "Date" ,
        y = "Price" ,
        hue = "Type" ,
        marker = "o"
    )

    plt.title("Stock Price Prediction - Next 7 Business Days")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()

    return forecast
