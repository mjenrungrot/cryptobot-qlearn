import requests
import datetime
import pandas as pd
import io
import os

key = os.environ["CRYPTO_KEY"]

headers = {'X-CoinAPI-Key': key}

base = "https://rest.coinapi.io/v1/ohlcv/"

sym = "BITSTAMP_SPOT_BTC_USD"

start = datetime.date(2017, 1, 1)

end = start + datetime.timedelta(days=252)

response = requests.get(base + sym + "/history/", headers=headers,
                       params={"period_id": "1DAY",
                               "time_start": start.isoformat(),
                               "time_end": end.isoformat(),
                               "output_format": "csv",
                               "limit": 500})

df = pd.read_csv(io.StringIO(response.text), sep=";")
df.to_csv("{:}-{:}.csv".format(sym,start))
print(df.head())
