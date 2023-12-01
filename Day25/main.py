# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#
# weather_data = []
# for list_entry in data:
#     data_pur = list_entry.strip("\n")
#     weather_data.append(data_pur)
#
# print(weather_data)

# import csv
#
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

## Get Data in Row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


## Convert Celsius to fahrenheit

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday.temp * 9/5 + 32
# print(monday_temp_F)


## Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")





