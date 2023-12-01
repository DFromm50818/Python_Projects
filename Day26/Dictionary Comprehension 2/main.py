weather_c = eval(input()) #Input must be a Dict!

weather_f = {day: ((celsius * 9/5) + 32) for (day, celsius) in weather_c.items()}

print(weather_f)