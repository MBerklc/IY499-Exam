import matplotlib.pyplot as plt
import numpy as np
"""
Programmer: Muhammed Berk Kilic
Student ID: P2916144
"""
title = "Muhammed' s Graph App"
print(title)
menu = "1. Show weekly temperature example"
menu += "\n2. Random histogram example"
menu += "\n3. Markers example"
menu += "\n0. Exit\n"
line = "\n-------------------------------------"
choice = "47"

while choice != 0:
    print(menu)
    choice = input("Enter your choice: ")
    print(line)

    match choice:
        case "0":
            print(f"Exiting...{line}")
            break
            # ----------------------------------------------------------
        case "1":
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            temps = [12, 14, 13, 15, 20, 14, 13]
            plt.plot(days, temps)
            plt.title("Daily Temperature")
            plt.xlabel("Day")
            plt.ylabel("Temperature (°C)")
            plt.grid(True)
            plt.show()
            print(line)
            # -----------------------------------------------------------
        case "2":
            x = np.random.normal(170, 10, 250)

            plt.hist(x)
            plt.show()
            continue
            # -----------------------------------------------------------
        case "3":
            import matplotlib.pyplot as plt
            import numpy as np

            ypoints = np.array([3, 8, 1, 10])

            plt.plot(ypoints, marker='o')
            plt.show()
            continue
            # -----------------------------------------------------------
        case "4":
            continue
            # -----------------------------------------------------------
        case _:
            print(f"Invalid choice. Please try again.{line}")
