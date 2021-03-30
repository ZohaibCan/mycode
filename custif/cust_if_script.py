#!/usr/bin/env python3
message = 'The storm is '
wind = float(input("Provide the windspeed "))
if wind >= 25:
    print (message + "Severe")
elif wind <= 24:
    print(message + "moderate")

