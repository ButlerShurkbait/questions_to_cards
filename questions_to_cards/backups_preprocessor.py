#########################################################
# Written by: Zaid Asif
# Meant to be used in tandem with Matt Jackson's questions_to_cards program
# Flattens data structure of current qbreader backups
#
#
#
#########################################################

import json
import os

# TODO: Turn flattening into function
# TODO: Support database json files
# TODO: Category, year, difficulty filtering
# TODO: Write README file?
# TODO: Replace tabs with 4 spaces?

#SAMPLE_TOSSUP = json.loads("")
#SAMPLE_BONUS = json.loads("")


def intake():
    tossups, bonuses = [], []
    if 'data.json' in os.listdir():
        print("Reading data.json file from directory...")
        with open('data.json', 'r') as f:
            data = json.load(f)
        f.close()
        print("Reading complete.")
        print("Splitting questions into tossups and bonuses...")
        for tossup in data['tossups']:
            tossups.append(tossup)
        for bonus in data['bonuses']:
            bonuses.append(bonus)
        print("Complete.")
    else:
        print("No 'data.json' file found in directory. Continuing...")
    if 'tossups.json' in os.listdir():
        print("Reading tossups.json file from directory...")
        with open('tossups.json', 'r') as f:
            for line in f:
                tossups.append(json.loads(line))
        f.close()
        print("Reading complete.")
    else:
        print("No 'tossups.json' file found in directory. Continuing...")
    if 'bonuses.json' in os.listdir():
        print("Reading bonuses.json file from directory...")
        with open('bonuses.json', 'r') as f:
            for line in f:
                bonuses.append(json.loads(line))
        f.close()
        print("Reading complete.")
    else:
        print("No 'bonuses.json' file found in directory. Continuing...")
    return tossups, bonuses

tossups, bonuses = intake()
for bonus in bonuses:
    bonus['setName'] = bonus.get('set').get('name')
    bonus['setYear'] = bonus.get('set').get('year')
    bonus['type'] = "bonus"

for tossup in tossups:
    tossup['setName'] = tossup.get('set').get('name')
    tossup['setYear'] = tossup.get('set').get('year')
    tossup['type'] = "tossup"

with open('bonuses.json', 'w') as f:
    for bonus in bonuses:
        json.dump(obj=bonus,fp=f,separators=(',',':'))
        f.write('\n')
f.close()

with open('tossups.json', 'w') as f:
    for tossup in tossups:
        json.dump(obj=tossup,fp=f,separators=(',',':'))
        f.write('\n')
f.close()
