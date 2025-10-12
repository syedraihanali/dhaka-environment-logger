# 🌤️ Dhaka Environmental Data Logger

An automated, open-source system that records **hourly environmental data** for **Dhaka, Bangladesh**, including:

- ☁️ Weather (temperature, humidity, pressure, wind speed)
- 🌫️ Air quality (PM2.5, PM10, CO, NO₂, O₃, AQI)
- 🌞 UV index (ultraviolet radiation level)

The logger runs automatically using **GitHub Actions** and collects data from the **[OpenWeatherMap](https://openweathermap.org/api)** and **[OpenUV](https://www.openuv.io/)** APIs.  
All data is saved in both **JSON** and **CSV** formats, rotated monthly, and publicly available for analysis.

---

## 🧠 Features

✅ Automated hourly updates via GitHub Actions  
✅ Rotates files monthly (e.g. `environment_2025_10.json`)  
✅ Dual format output — JSON & CSV  
✅ Separate folders for clean organization  
✅ 100% free and serverless (no VPS needed)  
✅ Data suitable for analytics, visualization, or research  

---

## 🗂️ Project Structure

```
dhaka-environment-logger/
├── environment_logger.py
├── README.md
├── data/
│   ├── json/
│   │   └── environment_2025_10.json
│   └── csv/
│       └── environment_2025_10.csv
└── .github/
    └── workflows/
        └── environment.yml
```

---

## ⚙️ How It Works

1. **GitHub Actions** runs automatically every hour.
2. The Python script (`environment_logger.py`) fetches:
   - Weather data (temperature, humidity, pressure, wind)
   - Air pollution levels (PM2.5, PM10, etc.)
   - UV index
3. The script saves these in both JSON and CSV formats under `/data/json` and `/data/csv`.
4. Each new month, the logger creates a new set of files automatically.
5. The data is committed and pushed to GitHub.

---

## 🧩 Setup Instructions

### 1️⃣ Get Free API Keys

You’ll need two API keys:
- **OpenWeatherMap API** → [https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)
- **OpenUV API** → [https://www.openuv.io/](https://www.openuv.io/)

---

### 2️⃣ Add Secrets to Your GitHub Repository

1. Go to your repo → **Settings → Secrets and variables → Actions → New repository secret**
2. Add the following secrets:

| Secret Name | Description |
|--------------|-------------|
| `OPENWEATHER_API_KEY` | Your OpenWeatherMap API key |
| `OPENUV_API_KEY` | Your OpenUV API key |

---

### 3️⃣ Configure Author Info

Edit `.github/workflows/environment.yml` and replace:
```yaml
git config --global user.name "YOUR_GITHUB_USERNAME"
git config --global user.email "YOUR_VERIFIED_EMAIL@example.com"
```
➡ Use your **actual GitHub username and a verified email** (to make commits count toward your contribution graph).

---

### 4️⃣ Push Your Code

Once pushed, the workflow will start automatically at the next full hour (e.g., 1:00, 2:00, 3:00, etc.).  
You can also trigger it manually under **Actions → “Run workflow.”**

---

## 📊 Example Data Entry

```json
{
  "time": "2025-10-12T10:00:00Z",
  "city": "Dhaka, BD",
  "temp_c": 30.2,
  "humidity": 68,
  "pressure": 1005,
  "weather": "clear sky",
  "wind_speed": 3.5,
  "air_pm2_5": 62,
  "air_pm10": 98,
  "air_co": 300,
  "air_no2": 28,
  "air_o3": 40,
  "air_aqi": 4,
  "uv_index": 6.3
}
```

---

## 🕒 Data Collection Schedule

| Data Type | Frequency | Source |
|------------|------------|---------|
| Weather | Hourly | OpenWeatherMap |
| Air Quality | Hourly | OpenWeatherMap |
| UV Index | Hourly | OpenUV |
| File Rotation | Monthly | Auto-managed |

---

## 📁 Data Folders

```
data/
├── json/   → Hourly JSON logs per month
└── csv/    → Hourly CSV logs per month
```

Each month, new files (like `environment_2025_11.json` and `environment_2025_11.csv`) are automatically created.  

---

## 📈 Potential Uses

- 🌦️ Long-term environmental trend tracking  
- 🌫️ Air pollution & UV exposure analysis  
- 📊 Visualization dashboards (Chart.js, Grafana, etc.)  
- 🧠 Educational projects in data science or climate studies  
- 🤖 AI/ML modeling for weather and AQI prediction  

---

## 🧰 Tech Stack

- **Python 3.11**
- **GitHub Actions**
- **OpenWeatherMap API**
- **OpenUV API**
- **CSV & JSON for data storage**

---

## 🧑‍💻 Author

**[Syed Raihan Ali](https://github.com/syedraihanali)**  
💡 Built for open data, automation, and environmental awareness.  

---

## 📄 License

This project is licensed under the **MIT License**.  
You’re free to use, modify, and share it with proper attribution.

---

## ⭐ Support

If you find this project useful:
- ⭐ Star the repo on GitHub  
- 🔁 Fork it and try your own city  
- 🧩 Contribute improvements or dashboards  

---

### 🔍 Keywords

`Dhaka`, `Bangladesh`, `weather`, `air-quality`, `UV-index`, `environment`, `data-logger`, `automation`, `open-data`, `GitHub Actions`, `Python`
