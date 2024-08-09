# Project Requirements
# 1. Welcome Message: Display a welcome message to the user.
# // user_name = input("Thanks for checking out my weather app!\nWhat is your name? ")
# // print(f"Hello and welcome {user_name}, to the worlds..... ahem..... premium weather application.\nAll other weather apps pale in comparison!")

# 2. User Input: Ask for the city name for which the weather forecast is needed.
# // hosen_city = input("Which city would you like to know the weather of? ")

# TODO Create a function that incorporates the previous two tasks (task1, task2).

def weather_app():
  user_name = input("Thanks for checking out my weather app!\nWhat is your name?\n")
  print()
  print(f"Hello and welcome {user_name}, to the world's most..... ahem..... premium weather application.\nAll other weather apps pale in comparison!")
  
  while True: # Creates infinte loop until condition is met
    chosen_city = input("Which city would you like to know the weather? (or type 'exit' to quit)\n")
    chosen_city = chosen_city.title() # The title() method returns a string where the first character in every word is upper case.
    # ! CAVEAT. If the word contains a number or a symbol, the first letter after that will be converted to upper case !
    
    if chosen_city.lower() == 'exit':
      print("Thank you for using the world's most premium weather app. Toodle-Pip!")
      break
    print()
    get_weather_forecast(chosen_city)
    print()
    print()

# 3. Fetch Weather Data: Use hardcoded weather data for several cities to simulate fetching weather information.
weather_data = {"London": {"temperature": "15°C", "conditions": "Cloudy",
"wind_speed": "5 km/h", "humidity": "80%"}, "New York": {"temperature":
"20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity":
"50%"}, "Tokyo": {"temperature": "18°C", "conditions": "Rainy",
"wind_speed": "7 km/h", "humidity": "90%"}, "Sydney": {"temperature":
"22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity":
"60%"}, "Paris": {"temperature": "17°C", "conditions": "Foggy",
"wind_speed": "3 km/h", "humidity": "85%"}}

# 4. Display Weather Data:
# Current temperature
# // print(f"The temperature in {chosen_city} is {weather_data[chosen_city]["temperature"]}")

# Weather conditions (e.g., sunny, rainy)
# // print(f"The weather in {chosen_city} is {weather_data[chosen_city]["conditions"]}")

# Wind speed
# // print(f"The wind speed in {chosen_city} is {weather_data[chosen_city]["wind_speed"]}")

# Humidity
# // print(f"The humidity levels in {chosen_city} are {weather_data[chosen_city]["humidity"]}")

# 5. Data Validation: Ensure valid input by checking that the user enters a valid city name from the hardcoded list.
def get_weather_forecast(chosen_city):
  try:
    city_weather = weather_data[chosen_city]
    temperature = city_weather["temperature"]
    conditions = city_weather["conditions"]
    wind_speed = city_weather["wind_speed"]
    humidity = city_weather["humidity"]
    
    print(f"Today's weather forcast for {chosen_city}:")
    print(f"Temperature: {temperature}")
    print(f"Condition: {conditions}")
    print(f"Wind Speed: {wind_speed}")
    print(f"Humidity: {humidity}")
  except KeyError:
    print(f"Key Error! Weather data for {chosen_city} is not available")
  except Exception as :
    print("An unexpected error occurred: {e}")


# 6. Thank You Message: Thank the user for using the weather forecast application.
# * Completed!

# Design Considerations
# • Structure your program to include clear main functions and subroutines.
# • Ensure your code is modular and readable.
# • Handle invalid city names by informing the user and allowing them to try again.

weather_app()
