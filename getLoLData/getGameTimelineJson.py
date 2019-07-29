import json
from datetime import datetime

import utility

with open(utility.game_ids_file_path) as f_game_ids:
    game_ids = f_game_ids.readlines()

cnt = 0
game_ids_len = len(game_ids)

for game_id in game_ids:
    game_id = game_id.replace("\n", "")

    print("expected game_id json = " + game_id)
    timeline_json = utility.get_lol_game_timeline_json(utility.game_timeline_url, str(game_id))

    if timeline_json == "" or timeline_json == "429":
        print("skipped summonerId json = " + game_id)
        continue

    cnt += 1

    if cnt % 10 == 0:
        print(str(cnt) + " / " + str(game_ids_len) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    print(utility.game_timeline_directory_path + game_id + ".json")

    with open(utility.game_timeline_directory_path + game_id + ".json", "w") as f_json:
        try:
            json.dump(timeline_json, f_json, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getMatchjson] game_id = " + game_id)
            # give up getting json
