import json
import math
import pandas as pd


json_path = 'C:\\output\\game\\timeline\\202077381.json'

with open(json_path, 'r') as f_timelines:
    timelines = json.load(f_timelines)

    output_log = {}
    tmp = []

    for frame in timelines['frames']:
        if not frame['events']:
            continue

        for event in frame['events']:
        
            if event['type'] == 'BUILDING_KILL':
                # output_log['team_id'] = event['teamId']
                # output_log['timestamp'] = math.floor(event['timestamp'] / 1000)

                if event['teamId'] not in output_log:
                    output_log[event['teamId']] = {}

                # output_log[event['teamId']]['timestamp'] = event['timestamp']

                if event['laneType'] == 'BOT_LANE' and event['towerType'] == 'OUTER_TURRET':
                    output_log[event['teamId']]['bot_1st_tower'] = 1
                    output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'TOP_LANE' and event['towerType'] == 'OUTER_TURRET':
                    output_log[event['teamId']]['top_1st_tower'] = 1
                    output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'MID_LANE' and event['towerType'] == 'OUTER_TURRET':
                    output_log[event['teamId']]['mid_1st_tower'] = 1
                    output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'BOT_LANE' and event['towerType'] == 'INNER_TURRET':
                    output_log[event['teamId']]['bot_2nd_tower'] = 1
                    output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'TOP_LANE' and event['towerType'] == 'INNER_TURRET':
                    output_log[event['teamId']]['top_2nd_tower'] = 1
                    output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'MID_LANE' and event['towerType'] == 'INNER_TURRET':
                    output_log[event['teamId']]['mid_2nd_tower'] = 1
                    output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'BOT_LANE' and event['towerType'] == 'BASE_TURRET':
                    if 'bot_inhi_tower' not in output_log:
                        output_log[event['teamId']]['bot_inhi_tower'] = 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                    else:
                        output_log[event['teamId']]['bot_inhi_tower'] += 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'TOP_LANE' and event['towerType'] == 'BASE_TURRET':
                    if 'top_inhi_tower' not in output_log:
                        output_log[event['teamId']]['top_inhi_tower'] = 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                    else:
                        output_log[event['teamId']]['top_inhi_tower'] += 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'MID_LANE' and event['towerType'] == 'BASE_TURRET':
                    if 'mid_inhi_tower' not in output_log:
                        output_log[event['teamId']]['mid_inhi_tower'] = 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                    else:
                        output_log[event['teamId']]['mid_inhi_tower'] += 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'BOT_LANE' and event['buildingType'] == 'INHIBITOR_BUILDING' and event['towerType'] == 'UNDEFINED_TURRET':
                    if 'bot_inhi' not in output_log:
                        output_log[event['teamId']]['bot_inhi'] = 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                    else:
                        output_log[event['teamId']]['bot_inhi'] += 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'TOP_LANE' and event['buildingType'] == 'INHIBITOR_BUILDING' and event['towerType'] == 'UNDEFINED_TURRET':
                    if 'top_inhi' not in output_log:
                        output_log[event['teamId']]['top_inhi'] = 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                    else:
                        output_log[event['teamId']]['top_inhi'] += 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'MID_LANE' and event['buildingType'] == 'INHIBITOR_BUILDING' and event['towerType'] == 'UNDEFINED_TURRET':
                    if 'mid_inhi' not in output_log:
                        output_log[event['teamId']]['mid_inhi'] = 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                    else:
                        output_log[event['teamId']]['mid_inhi'] += 1
                        output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'MID_LANE' and event['towerType'] == 'NEXUS_TURRET':
                    output_log[event['teamId']]['nexus_tower'] = 1
                    output_log[event['teamId']]['timestamp'] = event['timestamp']

                elif event['laneType'] == 'MID_LANE' and event['towerType'] == 'UNDEFINED_TURRET':
                    output_log[event['teamId']]['nexus'] = 1
                    output_log[event['teamId']]['timestamp'] = event['timestamp']

    tmp.append(output_log)

    print(tmp)

    tmp_df_100 = pd.DataFrame(output_log[100].items())
    tmp_df_100['team_id'] = 100
    tmp_df_100['game_id'] = 202077381
    # tmp_df_100.to_csv('test2.csv', mode='a', index=False, header=False)

    tmp_df_200 = pd.DataFrame(output_log[200].items())
    tmp_df_200['team_id'] = 200
    tmp_df_200['game_id'] = 202077381
    # tmp_df_200.to_csv('test2.csv', mode='a', index=False, header=False)

    df = pd.concat([tmp_df_100, tmp_df_200])
    # df.columns = ['build_type', 'break_amount', 'team_id', 'game_id']
    df.to_csv('test3.csv',index=False, header=True)

    
