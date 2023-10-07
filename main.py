# task 1 weather checking command line application

# ---------------importing necessary libraries----------------------------
import requests
import json
import time

# ---------------my weather api key----------------------------
api_key = '7a0df26708d9ab9b8feecf931162b780'

# -------------weather api url---------------------------------
url = 'http://api.openweathermap.org/data/2.5/weather'

favourite_cities = []


def get_weather(city):  # -----------------------function to get weather details using city name -------------------
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:                    # --------------------error handling using try and except starts here-----------------------
        response = requests.get(url, params=params)
        weather_data = response.json()
        return weather_data
    except:
        # ----error message with status code ------
        print(
            f"Error: Unable to fetch data. Status code {response.status_code}")

    # --------------------error handling using try and except ends here-----------------------


def add_favourite_city():  # ---------------function to add city to favourite city list---------------------------
    city_name = input("Enter the city name you want to add to favourites")
    favourite_cities.append(city_name)
    print(f"{city_name} added to favourite")


def remove_favourite_city():  # ------------------function to remove city fom favourite city list------------
    if not favourite_cities:
        print(f"your favourite cities list is empty")
    else:
        print("Your Favourite Cities are:-")
        for i, city in enumerate(favourite_cities):
            print(f"{i+1}. {city}")

        while True:
            try:  # --------------------error handling using try and except starts here-----------------------
                city_index = int(
                    input("select the city number you want to remove it"))-1
                if city_index >= 0 and city_index < len(favourite_cities):
                    removed_city = favourite_cities.pop(city_index)
                    print(f"{removed_city} removed from your favourite city list")
                    break
                else:
                    print("invalid choice. Please enter a valid choice. !!!!!")
            except:
                # ----error message ------
                print("Invalid input. Please enter a valid input. !!!!!")

            # --------------------error handling using try and except ends here-----------------------


def display_favourite_city():  # --------------defining display favourite city function here--------
    if not favourite_cities:
        print(f"your favourite cities list is empty")
    else:
        print("Your Favourite Cities are:-")
        # ---------printing favourite cities using for loop with index starting from 1-------
        for i, city in enumerate(favourite_cities):
            print(f"{i+1}. {city}")


def main():  # --------defining main function here--------

    while True:
        print("------------------wheather checking application---------------------")
        print("1.check weather by city name")
        print("2.Add a city to favourites")
        print("3.Remove a city from favourites")
        print("4.Display favourite cities")
        print("5.Exit")

        # ------taking user choice---------
        choice = int(input("--Select an option: "))

        if choice == 1:  # --------checking user choice for 1---------
            city_name = input("--enter city name: ")
            weather_data = get_weather(city_name)
            if weather_data:
                # ----checking condition wether weather and main exist in weather data or not------
                if "weather" in weather_data and "main" in weather_data:
                    print(
                        f"Weather in {city_name}: {weather_data['weather'][0]['description']}")
                    print(f"temperature: {weather_data['main']['temp']} °C")
                    print(
                        f"feels like: {weather_data['main']['feels_like']} °")
                    print(f"Humidity:{weather_data['main']['humidity']}% ")
            else:
                print("Invalid weather data. Please try again.!!!")

        elif choice == 2:            # --------checking user choice for 2---------
            add_favourite_city()

        elif choice == 3:  # --------checking user choice for 3---------
            remove_favourite_city()

        elif choice == 4:  # --------checking user choice for 4---------
            display_favourite_city()

        elif choice == 5:  # --------checking user choice for 5---------
            print("Thank for your time. Have a nice day.!!")
            break
        else:  # --------else part will show that user has given wrong input---------
            print("invalid choice. Please enter a valid choice. !!!!!")

        # ---------refreshing entire code after 15 seconds--------
        refresh_interval = 15 * (int(time.time()) % 2)
        print(f"Refreshing in {refresh_interval} seconds...")
        time.sleep(refresh_interval)


main()  # calling main function here
