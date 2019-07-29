import json
# from datetime import datetime
import datetime
import time
import math

import utility

with open(utility.game_ids_file_path) as f_game_ids:
    game_ids = f_game_ids.readlines()

cnt = 0
game_ids_len = len(game_ids)

end_ut = math.floor(time.time()) * 1000
first_ut = end_ut - (60 * 60 * 24 * 60 * 1000)

print(datetime.date.fromtimestamp(first_ut / 1000).strftime("%m-%d-%y"))
print(datetime.date.fromtimestamp(end_ut / 1000).strftime("%m-%d-%y"))

for game_id in game_ids:
    game_id = game_id.replace("\n", "")

    print("expected game_id json = " + game_id)
    game_info_json = utility.get_lol_game_info_json(utility.game_info_url, str(game_id))

    if game_info_json == "" or game_info_json == "429":
        print("skipped summonerId json = " + game_id)
        continue

    if not (first_ut <= game_info_json['gameCreation'] <= end_ut):
        print('finished because refrain getting past data')
        break

    cnt += 1

    if cnt % 10 == 0:
        print('{0} / {1}, {2}'.format(cnt, game_ids_len, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

    print(utility.game_info_directory_path + game_id + ".json")

    with open(utility.game_info_directory_path + game_id + ".json", "w") as f_json:
        try:
            json.dump(game_info_json, f_json, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getMatchjson] game_id = " + game_id)
            # give up getting json
