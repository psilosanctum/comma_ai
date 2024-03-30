import requests
import pandas as pd
import time
import os
pd.set_option('display.max_columns', None)

s = requests.session()
TOKEN = os.environ['COMMA_AI_KEY']
headers = {
    'Authorization': 'JWT {}'.format(TOKEN)
}
# resp = s.get("https://api.commadotai.com/v1/me/devices/", headers=headers)
# resp = s.get("https://api.commadotai.com/v1.1/devices/1a07a89695e502c8/", headers=headers)
# resp = s.get("https://api.commadotai.com/v1/devices/1a07a89695e502c8/location", headers=headers)
# resp = s.get("https://api.commadotai.com/v1.1/devices/1a07a89695e502c8/stats", headers=headers)
resp = s.get("https://api.commadotai.com/v1/devices/1a07a89695e502c8/segments?from=1704607200", headers=headers)
data = resp.json()
df = pd.DataFrame(data)
# df.to_csv('route_data.csv', index=False)
print(df.head())
# resp = s.get("https://api.commadotai.com/v1/route/1a07a89695e502c8|2024-01-23--16-56-52/", headers=headers)
# print(resp.text)
# resp = s.get("https://api.commadotai.com/v1/route/1a07a89695e502c8|2024-01-23--16-56-52/files", headers=headers)
# print(resp.text)
# print(resp.json()[1])


