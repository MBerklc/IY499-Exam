'''
Programmer: Muhammed Berk Kilic
Student ID: P296144
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  statistics
import os

#Get data and save into csv file using pandas
def get_user_data():
    isEnough = False
    while not isEnough:
        try:
            print("For exit input '0'")
            age = int(input("Enter age: "))
            if age == 0:
                isEnough = True
            elif age < 0 or age > 125:
                print("Number should be between 0 to 125. For exiting 0")
            else:
                df = pd.DataFrame([[age]], columns=["Age"])
                header = not os.path.exists("sampleData-1.csv") #Write header only on first save
                df.to_csv("sampleData-1.csv", mode='a', header=header, index=False)
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

#Ask user to specify class width for grouping
def get_bin_width():
    while True:
        try:
            width = int(input("Enter class width (e.g. 10): "))
            if width > 0:
                return width
            print("Width must be positive")
        except ValueError:
            print("Wrong input enter a number")

#Compute mean, median, mode, modal class, variance, standard deviation using statistics
def compute_statistics(data):
    ages = list(data["Age"])

    print("---Statistics---")
    print("Mean:", statistics.mean(ages))
    print("Median:", statistics.median(ages))

    try:
        print("Mode:", statistics.mode(ages))
    except statistics.StatisticsError:
        print("Mode: No unique mode")

    # Using numpy get variance and std dev
    print("Variance:", np.var(ages))
    print("Std Dev:", np.std(ages))

    # Build bins based on user width and data range
    width = get_bin_width()
    start = (min(ages) // width) * width
    stop = ((max(ages) // width) + 2) * width
    bins = list(range(start, stop, width))

    grouped = pd.cut(data["Age"], bins=bins, right=False)
    freq = grouped.value_counts().sort_index()

    # Build frequency table with midpoint and cumulative frequency
    rows = []
    cumulative = 0
    for interval, count in freq.items():
        midpoint = (interval.left + interval.right) / 2
        cumulative += count
        rows.append({"Class": str(interval), "Midpoint": midpoint, "Frequency": count, "Cumulative": cumulative})

    table_df = pd.DataFrame(rows)
    print("\n---Grouped Data---")
    print(table_df.to_string(index=False))
    print("Modal Class:", freq.idxmax())

    table_df.to_csv("results.csv", index=False)
    print("Results saved to results.csv")

#Draw a histogram from grouped data using matplotlib
def draw_histogram(grouped_df, bins):
    plt.hist(grouped_df, bins=bins, edgecolor='black')
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.xticks(bins) #Label each bin edge on x-axis
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

        # Handle user menu choice
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
                width = get_bin_width()
                ages = list(df["Age"])
                start = (min(ages) // width) * width
                stop = ((max(ages) // width) + 2) * width
                bins = list(range(start, stop, width))
                draw_histogram(df["Age"], bins)
                print(line)
            # -----------------------------------------------------------

            case _:
                print(f"Invalid choice. Please try again.{line}")


#For show there is only one main and run
if __name__ == "__main__":
    main()