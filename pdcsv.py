import pandas as pd


import os
print(os.getcwd())
# Out: /Users/shane/Documents/blog
# Display all of the files found in your current working directory

print(os.listdir(os.getcwd()))
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("vkbook.csv")
# Preview the first 5 lines of the loaded data
print(data.head())
print("hello")