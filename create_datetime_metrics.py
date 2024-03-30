import pandas as pd
import time
pd.set_option('display.max_columns', None)

daily_dates = pd.date_range('2024-01-01', '2026-12-31', freq ='D').tolist()
week_day = []
week_number = []
daily_date_str = []
convert_unix = []
for i in daily_dates:
    str_dt = pd.to_datetime(i).strftime("%Y-%m-%d")
    converted_day = pd.Timestamp(i).day_of_week
    week_number.append(i)
    daily_date_str.append(str_dt)
    week_day.append(converted_day)
    unix = (time.mktime(i.timetuple()))
    convert_unix.append(unix)

daily_dates_df = pd.DataFrame()
daily_dates_df['dates'] = daily_date_str
daily_dates_df['day_of_week'] = week_day
daily_dates_df['datetime_obj'] = week_number
daily_dates_df['week_number'] = daily_dates_df['datetime_obj'].dt.isocalendar().week
daily_dates_df['unix'] = convert_unix
daily_dates_df['unix'] = daily_dates_df['unix'].astype(int)
daily_dates_df = daily_dates_df[['unix', 'dates', 'datetime_obj', 'week_number', 'day_of_week']]
print(daily_dates_df)
