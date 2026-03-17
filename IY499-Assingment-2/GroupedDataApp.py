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
    # create pandas Dataframe with column name
    df = pd.DataFrame(data, columns=["ID", "Weight", "Age"])
    # Save the Dataframe into a CSV file
    # index=False argument ensures that the DataFrame's index is not included in the CSV file.
    df.to_csv("sampleData-1.csv", index=True)
    print("numerical Data saved in a csv file, called sampleData-1")
    print("Data Saved")

#Read numerical data from csv file using pandas
def read_data():
    df = pd.read_csv("sampleData-1.csv")
    print("\n**** Data from CSV file  ****\n")
    print(df)
    print(df.describe())
    print("Data was loaded")
    return df

#Compute mean, median, mode, modal class, variance, standard deviation using statistics
def compute_statistics(data, grouped_df, frequency, midpoint):
    print("Display all statistics")

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
                read_data()
                compute_statistics("data", "grouped_df", "frequency", "midpoint")
                print(line)
            # -----------------------------------------------------------
            case "3":
                df = read_data()
                draw_histogram(df["Weight"])
                draw_histogram(df["Age"])
                print(line)
            # -----------------------------------------------------------

            case _:
                print(f"Invalid choice. Please try again.{line}")


#For show there is only one main and run
if __name__ == "__main__":
    main()