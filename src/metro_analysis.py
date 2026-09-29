import pandas as pd
import numpy as np

file_paths = '..data\challenge_dataset_chennai_metro_station_activity.csv'
metro_data = pd.read_csv(file_paths)

south_stations = metro_data[metro_data['zone']  == 'South' ]
print(south_stations)

multi_cndtn = metro_data[(metro_data['daily_entries'] > 10000) & (metro_data['peak_hour_load_pct']> 60 )]
print(multi_cndtn)

multi_or = metro_data[(metro_data['daily_entries'] > 15000) | (metro_data['monthly_complaints']> 30 )]
print(multi_or)

metro_copy = metro_data.copy()
spcfc_cols = metro_copy.loc[metro_copy['zone'] == 'Central',
                       [ 'station_name',
                        'zone',
                        'daily_entries',
                        'avg_wait_minutes']
                            ]
print(spcfc_cols)

longest_waiting_time = metro_copy.loc[metro_copy['avg_wait_minutes'].idxmax(),
                                  'station_name']
print("station with longest waiting time is :",longest_waiting_time)

no_parking = metro_copy.loc[metro_copy['has_parking'] == False,
                        'station_name']
print(no_parking)
print("Stations with parking:", (metro_data['has_parking'] == True).sum())
print("Stations without parking:", (metro_data['has_parking'] == False).sum())
metro_copy['total_weekly_delays'] = (metro_copy['weekday_delays'] + metro_copy['weekend_delays'])
result = metro_copy[['station_name','total_weekly_delays']]
print(result)

#data cleaning

missing_values = metro_copy.loc[
    metro_copy.isnull().any(axis=1)
]
print(missing_values)

average_waiting_time = metro_copy['avg_wait_minutes'].mean()
metro_copy['avg_wait_minutes'] = metro_copy['avg_wait_minutes'].fillna(
    average_waiting_time
)
median_complaints = metro_copy['monthly_complaints'].median()
metro_copy['monthly_complaints'] = metro_copy['monthly_complaints'].fillna(
    median_complaints   )

print(metro_copy[['avg_wait_minutes','monthly_complaints']].isnull().sum())

#groupby() practice

average_waiting_time_by_zone = (
    metro_copy.groupby('zone')['avg_wait_minutes'].mean()
)                               
print(average_waiting_time_by_zone)

max_daily_entries_zone =(
    metro_copy.groupby('zone')['daily_entries'].max()
)
print(max_daily_entries_zone)

number_of_stations = (metro_copy.groupby('zone')['station_name'].count()
                      )
print(number_of_stations)

multiple_statistics =(metro_copy.groupby('zone').agg(
    mean_daily_entries=('daily_entries','mean'),
    maximum_daily_entries=('daily_entries','max'),
    minimum_daily_entries=('daily_entries','min'),
    mean_avg_wait_minutes=('avg_wait_minutes','mean')

)
.reset_index()
                      )
print(multiple_statistics)

#numpy + pandas
entries_exit_array = metro_copy[['daily_entries','daily_exits']].to_numpy()
print(entries_exit_array.shape)

entry = metro_copy['daily_entries'].to_numpy()
exit = metro_copy['daily_exits'].to_numpy()
difference = entry - exit
print(difference)

max_entry_exit_difference = difference.max()
max_index = np.argmax(difference)
print("maiximum difference", max_entry_exit_difference)

station =metro_copy.loc[
    max_index,
    ['station_name','daily_entries','daily_exits']
]
print(station)

total_entry =entry.sum()
total_exit =exit.sum()
entry_exit_ratio = total_entry / total_exit
print(entry_exit_ratio)

#mini data-analysis questions

busiest_10_stations = metro_copy.sort_values('daily_entries',
                                             ascending=False).head(10)
print(busiest_10_stations[['station_name','daily_entries']])

problem_stations = metro_copy.loc[
    (metro_copy['monthly_complaints'] > 20) &
    (metro_copy['avg_wait_minutes'] > 3),
    ['station_name','monthly_complaints', 'avg_wait_minutes']
]
print(problem_stations)

metro_copy['entry_rank'] = (metro_copy['daily_entries'].rank(
    ascending=False).astype(int)
)
metro_copy = metro_copy.sort_values('entry_rank')

print(
    metro_copy[
        ['station_name', 'daily_entries', 'entry_rank']
    ]
)

zone_summary =(metro_copy.groupby('zone').agg(
    number_of_stations=('station_name','count'),
    average_entry=('daily_entries','mean'),
    average_exits=('daily_exits','mean'),
    average_waiting_time=('avg_wait_minutes','mean'),
    total_complaints=('monthly_complaints','sum')
)
)
print(zone_summary)

attention = metro_copy.copy()
attention['entries_rank'] = attention['daily_entries'].rank(
    ascending=True
)
attention['complaints_rank'] = attention['monthly_complaints'].rank(
    ascending=True
)
attention['waiting_rank'] = attention['avg_wait_minutes'].rank(
    ascending=True
)
attention['attention_score'] =(
    attention['entries_rank'] +
    attention['complaints_rank'] +
    attention['waiting_rank']
    ) 
most_attention = (
    attention.sort_values('attention_score', ascending=False) .head(10)
)
print()
print(
    most_attention[
        [
            'station_name',
            'zone',
            'daily_entries',
            'avg_wait_minutes',
            'monthly_complaints',
            'attention_score'
        ]
    ]
)
