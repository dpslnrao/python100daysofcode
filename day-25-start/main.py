# import csv
#
# def read_csv_to_list(file_path):
#     data_list = []
#     with open(file_path, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for row in csv_reader:
#             data_list.append(row)
#     return data_list
#
# # Example usage
# file_path = 'weather_data.csv'
# csv_data = read_csv_to_list(file_path)
# print(csv_data)


import pandas as pd
import numpy as np

data =pd.read_csv("weather_data.csv")
print(data)
print(data.to_dict())
print(data["temp"].to_list())
print(data["temp"].max())
print(data[data["day"] == "Saturday"] )