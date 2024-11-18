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

#SAMPLE_TOSSUP = json.loads("{"_id": {"$oid": "0"}, "question": "tossup body.", "answer": "answer", "subcategory": "sample_subcat", "category": "sample_category", "packet": {"_id": {"$oid": "0"}, "name": "1", "number": {"$numberInt": "1"}}, "set": {"_id": {"$oid": "0"}, "name": "1970 Sample Packet", "year": {"$numberInt": "1970"}, "standard": true}, "createdAt": {"$date": {"$numberLong": "0"}}, "updatedAt": {"$date": {"$numberLong": "0"}}, "difficulty": {"$numberInt": "1"}, "number": {"$numberInt": "1"}, "answer_sanitized": "answer", "question_sanitized": "tossup body."}")
#SAMPLE_BONUS = json.loads("{"_id":{"$oid":"0"},"leadin":"leadin","answers":["answer1","answer2","answer3"],"parts":["bonus part 1","bonus part 2","bonus part 3"],"subcategory":"sample_subcat","category":"sample_category","packet":{"_id":{"$oid":"0"},"name":"1","number":{"$numberInt":"1"}},"set":{"_id":{"$oid":"0"},"name":"1970 Sample Packet","year":{"$numberInt":"2000"},"standard":true},"createdAt":{"$date":{"$numberLong":"0"}},"updatedAt":{"$date":{"$numberLong":"0"}},"difficulty":{"$numberInt":"1"},"values":[{"$numberInt":"10"},{"$numberInt":"10"},{"$numberInt":"10"}],"alternate_subcategory":"sample_alternate_subcat","number":{"$numberInt":"1"},"answers_sanitized":["answer1","answer2","answer3"],"leadin_sanitized":"leadin","parts_sanitized":["bonus part 1","bonus part 2","bonus part 3"]}")


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
