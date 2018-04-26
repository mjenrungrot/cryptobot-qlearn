import requests
import datetime
import pandas as pd
import io
import os

key = os.environ["CRYPTO_KEY"]

headers = {'X-CoinAPI-Key': key}

base = "https://rest.coinapi.io/v1/ohlcv/"

sym = "BITSTAMP_SPOT_BTC_USD"

today = datetime.date.today()

week_ago = today - datetime.timedelta(days=int((500*4)/24))

response = requests.get(base + sym + "/history/", headers=headers,
                       params={"period_id": "4HRS",
                               "time_start": week_ago.isoformat(),
                               "output_format": "csv",
                               "limit": 500})

df = pd.read_csv(io.StringIO(response.text), sep=";")
df.to_csv("{:}-{:}.csv".format(sym,today))
print(df.head())
