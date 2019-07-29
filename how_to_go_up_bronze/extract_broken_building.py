import json
import math
import pandas as pd


json_path = 'C:\\output\\game\\timeline\\202077381.json'

df = pd.DataFrame(index=[], columns=['gameId', 'teamId', 'laneType', 'buildingType', 'towerType', 'timestamp'])

with open(json_path, 'r') as f_timelines:
    timelines = json.load(f_timelines)

    # # # output_log = {}
    # # # tmp = []

    x = 0

    for frame in timelines['frames']:
        if not frame['events']:
            continue

        for event in frame['events']:
        
            if event['type'] == 'BUILDING_KILL':
                # output_log['team_id'] = event['teamId']
                # output_log['timestamp'] = math.floor(event['timestamp'] / 1000)

                print(x)
                x = x + 1
 
                df = df.append(pd.Series([202077381, event['teamId'], event['laneType'], event['buildingType'], event['towerType'], event['timestamp']], index=df.columns), ignore_index=True)

print(df)
df.to_csv('ajfkajka.csv')
# df.to_csv('test3.csv',index=False, header=True)