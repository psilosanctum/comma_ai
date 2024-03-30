import pandas as pd
from datetime import datetime
pd.set_option('display.max_columns', None)

df = pd.read_csv('data/route_data.csv')
df['end_time'] = df['end_time_utc_millis'].__truediv__(1000).astype(int)
converted_date_list = []
for unix_time in df['end_time']:
    date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
    converted_date_list.append(date)
df['date'] = converted_date_list
df = df[['canonical_name', 'canonical_route_name', 'create_time', 'end_time', 'date', 'start_time_utc_millis', 'end_time_utc_millis', 'start_lat', 'end_lat', 'start_lng', 'end_lng', 'length']]
# print(df)
df['time_diff_millis'] = df['end_time_utc_millis'] - df['start_time_utc_millis']
df['time_diff_seconds'] = df['time_diff_millis'].__truediv__(1000)
df['time_diff_minutes'] = df['time_diff_seconds'].__truediv__(60)
df['time_diff_hours'] = df['time_diff_minutes'].__truediv__(60)
# print(df)
df = df.groupby(['canonical_route_name']).sum(numeric_only=True)[['length', 'time_diff_seconds', 'time_diff_minutes', 'time_diff_hours']].reset_index().sort_values('length', ascending=False)
# print(df.head(25))
df = df.loc[df['length'] > 0.01]

avg_trip_length = df['length'].mean().round(2)
avg_trip_time = df['time_diff_minutes'].mean().round(2)
longest_trip_miles = df['length'].max().round(2)
longest_trip_time = df['time_diff_hours'].max().round(2)
total_trips = df['canonical_route_name'].count()
total_miles = df['length'].sum().round(2)
total_hours = df['time_diff_hours'].sum().round(2)
print("Average trip length: ", avg_trip_length, 'miles')
print("Average trip time: ", avg_trip_time, 'minutes')
print('Longest trip: ', longest_trip_miles, 'miles')
print('Longest trip: ', longest_trip_time, "hours")
print('Total trips: ', total_trips)
print('Total miles: ', total_miles)
print('Total hours: ', total_hours)