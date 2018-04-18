import requests
import datetime
import pandas as pd
import io

key = "5D529B2D-63DA-48DD-ADE6-197F4EC47FFA"

headers = {'X-CoinAPI-Key': key}

base = "https://rest.coinapi.io/v1/ohlcv/"

sym = "BITSTAMP_SPOT_BTC_USD"

today = datetime.date.today()

week_ago = today - datetime.timedelta(days=7)

response = requests.get(base + sym + "/history/", headers=headers,
                       params={"period_id": "4HRS",
                               "time_start": week_ago.isoformat(),
                               "output_format": "csv"})

df = pd.read_csv(io.StringIO(response.text), sep=";")
print(df.head())
