import pandas as pd
import time
pd.set_option('display.max_columns', None)

wkly_date_range = pd.date_range('2024-01-01', '2026-12-31', freq ='W').tolist()
daily_dates = pd.date_range('2024-01-01', '2026-12-31', freq ='D').tolist()
# print(daily_dates)
convert_dt_unix = []
convert_dt_str = []
datetime_format = []
for i in wkly_date_range:
    datetime_format.append(i)
    str_dt = pd.to_datetime(i).strftime("%Y-%m-%d")
    unix = (time.mktime(i.timetuple()))
    convert_dt_unix.append(unix)
    convert_dt_str.append(str_dt)

time_df = pd.DataFrame()
time_df['unix'] = convert_dt_unix
time_df['unix'] = time_df['unix'].astype(int)
time_df['str'] = convert_dt_str
time_df['datetime_obj'] = datetime_format
time_df['week_number'] = time_df['datetime_obj'].dt.isocalendar().week

week_day = []
for i in time_df['str']:
    converted = pd.Timestamp(i).day_of_week
    week_day.append(converted)
# print(week_day)
# time_df['day_number'] = pd.Timestamp(time_df['str']).day_of_week
# print(time_df)