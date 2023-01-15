"""
inside the link was like that
{
  "fear_and_greed": {
    "score": 57.1714285714286,
    "rating": "greed",
    "timestamp": "2023-01-12T23:59:56+00:00",
    "previous_close": 54.4285714285714,
    "previous_1_week": 42.6,
    "previous_1_month": 58.7714285714286,
    "previous_1_year": 55.94285714285714
  },
  "fear_and_greed_historical": {
    "timestamp": 1673567996000.0,
    "score": 57.1714285714286,
    "rating": "greed",
    "data": [
      {
        "x": 1613001600000.0,
        "y": 76.0,
        "rating": "extreme greed"
      }
}

"""

from datetime import date,datetime,timedelta
import requests,json,csv,pytz

START_DATE = "2021-01-25"
BASE_URL="www.example.com"
r = requests.get("{}/{}".format(BASE_URL, START_DATE))
data = r.json()

print(json.dumps(data, indent=2))
fg_data = data['fear_and_greed_historical']['data']
fear_greed_values = {}
with open("fear-greed", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date,Fear Greed',"Rating"])
    for data in fg_data:
        dt = datetime.fromtimestamp(data['x'] / 1000, tz=pytz.utc)
        fear_greed_values[dt.date()] = int(data['y'])
        writer.writerow([dt.date(), int(data['y']), str(data['rating'])])

