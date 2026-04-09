'''
Programmer: Muhammed Berk Kilic
Student ID: P2916144
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  statistics

#Get data and save into csv file using pandas
def get_user_data():
    isEnough = False
    while not isEnough:
        try:
            print("For exit input '0'")
            age = int(input("Enter age: "))
            if age == 0:
                isEnough = True
            elif age < 0 or age > 150:
                print("Number should be between 0 to 150. For exiting 0")
            else:
                df = pd.DataFrame([[age]], columns=["Age"])
                df.to_csv("sampleData-1.csv", mode='a', header=False, index=False)
                print("Data Saved")
        except ValueError:
            print("Wrong input enter a number")

#Read numerical data from csv file using pandas
def read_data():
    df = pd.read_csv("sampleData-1.csv")
    print("\n**** Data from CSV file ****\n")

    ages = df["Age"].tolist()
    for i in range(0, len(ages), 5):
        print(*ages[i:i+5])   # 5 numbers per line

    print("\nData was loaded")
    return df

#Compute mean, median, mode, modal class, variance, standard deviation using statistics
def compute_statistics(data):
    ages = list(data["Age"])

    print("---Statistics---")
    print("Mean:", statistics.mean(ages))
    print("Median:", statistics.median(ages))

    try:
        print("Mode:", statistics.mode(ages))
    except:
        print("Mode: No unique mode")

    print("Variance:", statistics.variance(ages))
    print("Std Dev:", statistics.stdev(ages))

    # Grouping
    bins = [0, 10, 20, 30, 40, 50, 60]
    grouped = pd.cut(data["Age"], bins=bins)

    freq = grouped.value_counts().sort_index()

    print("\n---Grouped Data---")
    print(freq)

    print("Midpoints:", [(bins[i] + bins[i + 1]) / 2 for i in range(len(bins) - 1)])
    print("Modal Class:", freq.idxmax())

#Draw a histogram from grouped data using matplotlib
def draw_histogram(grouped_df):
    plt.hist(grouped_df)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()


def main():
    title = "---Group Data Application---"
    print(title)
    menu = "1. Add and save data"
    menu += "\n2. Show statistics"
    menu += "\n3. Draw histogram"
    menu += "\n0. Exit\n"
    line = "\n-------------------------------------"
    choice = "47"

    while choice != "0":
        print(menu)
        choice = input("Enter your choice: ")
        print(line)

        match choice:
            case "0":
                print(f"Exiting...{line}")
                break
            # ----------------------------------------------------------
            case "1":
                get_user_data()
                print(line)
            # -----------------------------------------------------------
            case "2":
                df = read_data()
                compute_statistics(df)
                print(line)
            # -----------------------------------------------------------
            case "3":
                df = read_data()
                draw_histogram(df["Age"])
                print(line)
            # -----------------------------------------------------------

            case _:
                print(f"Invalid choice. Please try again.{line}")


#For show there is only one main and run
if __name__ == "__main__":
    main()