Programmer: Muhammed Berk Kilic
P-number: P2916144

Declaration: This is my own work.

Description:
This program gets data from the user and saves it into a CSV file (if there 
is no CSV file it creates one). It shows statistics of the data and gets 
class width from the user to show grouped frequency table, and it shows a 
histogram with customisable class width.

Required Libraries:
pandas, numpy, matplotlib, statistics, os

Installation:
pip install pandas numpy matplotlib
(statistics and os are built into Python, no installation needed)

Usage:
Run the program with: python grouped_data_analysis.py
1. Add and save data   - enter age values one by one
2. Show statistics     - shows mean, median, mode, variance, std dev and frequency table
3. Draw histogram      - shows histogram of the data
0. Exit                - exits the program
