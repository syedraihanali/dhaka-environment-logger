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
timestamp = local_now.strftime("%Y-%m-%d %I:%M:%S %p BDT")

os.makedirs("data/json", exist_ok=True)
os.makedirs("data/csv", exist_ok=True)

json_file = f"data/json/environment_{month_tag}.json"
csv_file = f"data/csv/environment_{month_tag}.csv"

REQUEST_TIMEOUT = 10

def _safe_get_json(url, headers=None):
    """GET a URL and return JSON, or raise a RuntimeError with context on failure."""
    try:
        resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Request timed out after {REQUEST_TIMEOUT}s: {url}")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"HTTP {e.response.status_code} for {url}: {e.response.text[:200]}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed for {url}: {e}")
    except ValueError as e:
        raise RuntimeError(f"Invalid JSON response from {url}: {e}")

weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY_WEATHER}&units=metric"
weather = _safe_get_json(weather_url)

air_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY_WEATHER}"
air = _safe_get_json(air_url)
if not air.get("list"):
    raise RuntimeError(f"Unexpected air-pollution response (no 'list' key): {air}")
air_values = air["list"][0]["components"]

headers = {"x-access-token": API_KEY_UV}
uv_url = f"https://api.openuv.io/api/v1/uv?lat={LAT}&lng={LON}"
uv = _safe_get_json(uv_url)
if "result" not in uv or "uv" not in uv.get("result", {}):
    raise RuntimeError(f"Unexpected UV response: {uv}")

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
if os.path.exists(json_file) and os.path.getsize(json_file) > 0:
    with open(json_file, "r") as jf:
        try:
            data = json.load(jf)
        except json.JSONDecodeError:
            data = []
else:
    data = []

data.append(entry)

with open(json_file, "w") as jf:
    json.dump(data, jf, indent=2)

file_exists = os.path.isfile(csv_file)
with open(csv_file, "a", newline="") as cf:
    writer = csv.DictWriter(cf, fieldnames=list(entry.keys()))
    if not file_exists:
        writer.writeheader()
    writer.writerow(entry)

print("✅ Logged Dhaka environment data (local time):", timestamp)
