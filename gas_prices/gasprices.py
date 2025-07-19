import webbrowser
import tkinter as tk

location = input("Enter a State Name: ")
location_final = location.replace(" ", "")

city = input("Enter a City Name: ")
city_final = city.replace(" ", "_")

url = location_final + "GasPrices.com" + "/" + city_final + "/index.aspx"

webbrowser.open("http://" + url)

if location is not None:
    print("Here is your personalized link: " + url)
else:
    print("Sorry, we couldn't find that location.")
      