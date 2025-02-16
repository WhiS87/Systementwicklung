import requests
import json


API = "993001f9eba9f83a0aab44c4c60a118d"
latitude = "50.93"
longtitude= "6.96"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longtitude}&units=metric&lang=de&appid={API}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    with open("data.json", "w", encoding="utf-8") as file :
        json.dump(data, file, ensure_ascii=False, indent=4)
        
    print("Die Daten wurden Gespeichert!")
else:
    print("Fehler beim Abrufen der Daten. Satuscode: ", response.status_code)