import os
import requests
import datetime
import json
import csv
import pytz

API_KEY_WEATHER = os.getenv("OPENWEATHER_API_KEY")
API_KEY_UV = os.getenv("OPENUV_API_KEY")
CITY = "Dhaka"
COUNTRY = "BD"
LAT, LON = 23.833435976686932, 90.42756821593022  # Coordinates for Dhaka

dhaka_tz = pytz.timezone("Asia/Dhaka")
local_now = datetime.datetime.now(dhaka_tz)
month_tag = local_now.strftime("%Y_%m")
timestamp = local_now.strftime("%Y-%m-%d %I:%M:%S %p %Z") 

os.makedirs("data/json", exist_ok=True)
os.makedirs("data/csv", exist_ok=True)

json_file = f"data/json/dhaka_environment_{month_tag}.json"
csv_file = f"data/csv/dhaka_environment_{month_tag}.csv"

weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY_WEATHER}&units=metric"
weather = requests.get(weather_url).json()

air_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY_WEATHER}"
air = requests.get(air_url).json()
air_values = air["list"][0]["components"]

headers = {"x-access-token": API_KEY_UV}
uv_url = f"https://api.openuv.io/api/v1/uv?lat={LAT}&lng={LON}"
uv = requests.get(uv_url, headers=headers).json()

entry = {
    "time_local": timestamp,
    "city": f"{CITY}, {COUNTRY}",
    "temp_c": weather["main"]["temp"],
    "humidity": weather["main"]["humidity"],
    "pressure": weather["main"]["pressure"],
    "weather": weather["weather"][0]["description"],
    "wind_speed": weather["wind"]["speed"],
    "air_pm2_5": air_values["pm2_5"],
    "air_pm10": air_values["pm10"],
    "air_co": air_values["co"],
    "air_no2": air_values["no2"],
    "air_o3": air_values["o3"],
    "air_aqi": air["list"][0]["main"]["aqi"],
    "uv_index": uv["result"]["uv"]
}

with open(json_file, "a") as jf:
    jf.write(json.dumps(entry) + "\n")

file_exists = os.path.isfile(csv_file)
with open(csv_file, "a", newline="") as cf:
    writer = csv.DictWriter(cf, fieldnames=list(entry.keys()))
    if not file_exists:
        writer.writeheader()
    writer.writerow(entry)

print("✅ Logged Dhaka environment data (local time):", timestamp)
