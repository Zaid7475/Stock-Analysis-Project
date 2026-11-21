from dispaly_data import display_data
from basic_stats import basic_stats
from price_analysis import price_analysis
from volume_analysis import volume_analysis
from trend_analysis import trend_analysis
from outlier_analysis import outlier_analysis
from daily_returns import daily_returns
from monthly_analysis import monthly_analysis
from yearly_analysis import yearly_analysis
from charts import stock_charts
from prediction import stock_prediction
from generate_report import generate_report


def main():


    df = None

    print("\n================")
    print("\nStock Analysis")
    print("==================")

    while True:

        print("\n======Main Menu=======")
        print("1. Display Data")
        print("2. Basic Stats")
        print("3. Price Analysis")
        print("4. Volume Analysis")
        print("5. Trend Analysis")
        print("6. Outlier Analysis")
        print("7. Daily Returns")
        print("8. Monthly Analysis")
        print("9. Yearly Analysis")
        print("10. Charts")
        print("11. prediction")
        print("12. Generate Report")
        print("13. Exit")

        choice = input("\nEnter ur choice:")

        if choice == "1":

            print("\n-----Display Data-----")
            df = display_data()

        elif choice == "2":

            if df is not None:

                print("\n-----Basic Stat------")
                basic_stats(df)
            else:

                print("\nPlease display data first!")

        elif choice == "3":
        
            print("\n-----Price Analysis------")
            price_analysis(df)

        elif choice == "4":
        
            print("\n-----Volume Analysis------")
            volume_analysis(df)

        elif choice == "5":
        
            print("\n-----Trend Analysis------")
            trend_analysis(df)

        elif choice == "6":
        
            print("\n-----Outlier Analysis------")
            outlier_analysis(df)

        elif choice == "7":
        
            print("\n-----Daily Returns------")
            daily_returns(df)

        elif choice == "8":
        
            print("\n-----Monthly Analysis------")
            monthly_analysis(df)

        elif choice == "9":
        
            print("\n-----Yearly Analysis------")
            yearly_analysis(df)

        elif choice == "10":
        
            print("\n-----Charts------")
            stock_charts(df)

        elif choice == "11":
        
            print("\n-----Prediction------")
            stock_prediction(df)

        elif choice == "12":
        
            print("\n-----Generate Report------")
            generate_report(df)

        elif choice == "13":
        
            print("\nThank you for using Stock Analysis!")
            break

        else:
             
             print("\nInvalid choice! Please enter 1-13")

if __name__ == "__main__":
    main()
 
        
