def get_weather_report() -> str:
    weather: str = input(
        "What is the weather?"
    )  # go ahead and make the variable the input. You don't necessarily have to ask the question elsewhere like in tea party.
    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
