import utility

# Output Master and Challenger summoner ids to a files
# 1. summonerChallenger.csv
# 2. summonerMaster.csv
#
# Then, They are combined to a file, summoners.csv with no duplicated ids

challenger_summoner_json = utility.get_lol_challenger_summoners_id_json()
grandmaster_summoner_json = utility.get_lol_grandmaster_summoners_id_json()
master_summoner_json = utility.get_lol_master_summoners_id_json()

# output challenger ids
with open(utility.summoners_file_path, 'w', encoding="UTF-8") as f_summoners:
    if challenger_summoner_json != "":
        with open(utility.challenger_summoners_file_path, 'w', encoding="UTF-8") as f_challengers:
            for summoner in challenger_summoner_json["entries"]:
                f_challengers.write(summoner["summonerId"] + "\n")
                f_summoners.write(summoner["summonerId"] + "\n")

# output grandmaster ids
with open(utility.summoners_file_path, 'a', encoding="UTF-8") as f_summoners:
    if grandmaster_summoner_json != "":
        with open(utility.grandmaster_summoners_file_path, 'w', encoding="UTF-8") as f_grandMasters:
            for summoner in grandmaster_summoner_json["entries"]:
                f_grandMasters.write(summoner["summonerId"] + "\n")
                f_summoners.write(summoner["summonerId"] + "\n")

# output master ids
with open(utility.summoners_file_path, 'a', encoding="UTF-8") as f_summoners:
    if master_summoner_json != "":
        with open(utility.master_summoners_file_path, 'w', encoding="UTF-8") as f_masters:
            for summoner in master_summoner_json["entries"]:
                f_masters.write(summoner["summonerId"] + "\n")
                f_summoners.write(summoner["summonerId"] + "\n")


# make unique summoner ids in a file
utility.delete_duplicated_records(utility.summoners_file_path, False)


