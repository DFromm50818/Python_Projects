import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ["Gray", "Cinnamon", "Black"]
counts = []

for color in colors:
    count = len(squirrel_data.loc[squirrel_data["Primary Fur Color"] == color])
    counts.append(count)

squirrel_count_data = pandas.DataFrame({f"Fur Color,": colors, "Count": counts})
squirrel_count_data.to_csv("squirrel_count.csv")
print(squirrel_count_data)



