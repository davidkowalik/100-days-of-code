import csv
import numpy as np
import pandas as pd


# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for raw in data:
#         if raw[1] != 'temp':
#             temperatures.append(int(raw[1]))

# print(temperatures)

# data = pd.read_csv("weather_data.csv")

# print((data[data.day == "Monday"].temp * 9 / 5) + 32 )

sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

print(sq_data["Primary Fur Color"])

color_dict = {"Fur Color" : ["Gray", "Cinnamon", "Black"],
              "Count" :[0, 0, 0],
              }


color_dict["Count"][0] = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
color_dict["Count"][1] = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
color_dict["Count"][2] = len(sq_data[sq_data["Primary Fur Color"] == "Black"])

fur_color = pd.DataFrame.from_dict(color_dict)
fur_color.to_csv("squirrel_count.csv")

print(fur_color)