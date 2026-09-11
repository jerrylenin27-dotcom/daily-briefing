import requests
import sys
import datetime

if len(sys.argv) != 2:
    sys.exit()
    
try:
    weather = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": sys.argv[1], 
            "appid": "16d1947513ef69efe26d38d951d5d6c8", 
            "units": "metric"
            }
        )
    
    if weather.status_code == 200:
        weather_data = weather.json()
        temperature = weather_data["main"]["temp"]
        
    else:
        temperature = "Unavailable"
        
    trivia = requests.get("https://opentdb.com/api.php", params={"amount": 1})
    trivia_data = trivia.json()

    for result in trivia_data["results"]:
        question = result["question"]
        answer = result["correct_answer"]
    
    now = datetime.datetime.now()
    formatted = now.strftime("%d-%m-%Y %H:%M")

    with open("briefing.txt", "w") as file:
        file.write(f"City: {sys.argv[1]}\n")
        file.write(f"Temperature: {temperature}\n")
        file.write(f"Question: {question}\n")
        file.write(f"Answer: {answer}\n")
        file.write(f"Date_Time: {formatted}\n")
        
except requests.exceptions.ConnectionError:
    print("No internet connection — stopping.")