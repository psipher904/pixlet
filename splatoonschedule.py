
#import packages
import json
from urllib.request import Request, urlopen

#declare url and request variables with correct user agent
url = 'https://splatoon3.ink/data/schedules.json'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

#request url and read response content
with urlopen(req) as response:
    body = response.read()

#parses json string and converts to dict
inkdata = json.loads(body)

#Turf War Stages
turfwarstage1 = (inkdata["data"]["regularSchedules"]["nodes"][0]["regularMatchSetting"]["vsStages"][0]["name"])
turfwarstage2 = (inkdata["data"]["regularSchedules"]["nodes"][0]["regularMatchSetting"]["vsStages"][1]["name"])


#Anarchy Series Mode and Stages
anarchyseriesmode = (inkdata["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][0]["vsRule"]["name"])
anarchyseriesstage1 = (inkdata["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][0]["vsStages"][0]["name"])
anarchyseriesstage2 = (inkdata["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][0]["vsStages"][1]["name"])

#Anarchy Open Mode and Stages
anarchyopenmode = (inkdata["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][1]["vsRule"]["name"])
anarchyopenstage1 = (inkdata["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][1]["vsStages"][0]["name"])
anarchyopenstage2 = (inkdata["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][1]["vsStages"][1]["name"])

#X Battle Mode and Stages
xbattlemode = (inkdata["data"]["xSchedules"]["nodes"][0]["xMatchSetting"]["vsRule"]["name"])
xbattlestage1 = (inkdata["data"]["xSchedules"]["nodes"][0]["xMatchSetting"]["vsStages"][0]["name"])
xbattlestage2 = (inkdata["data"]["xSchedules"]["nodes"][0]["xMatchSetting"]["vsStages"][1]["name"])


#Salmon Run Stage and Weapons
salmonstage = (inkdata["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["coopStage"]["name"])
srweapon1 = (inkdata["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["weapons"][0]["name"])
srweapon2 = (inkdata["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["weapons"][1]["name"])
srweapon3 = (inkdata["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["weapons"][2]["name"])
srweapon4 = (inkdata["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["weapons"][3]["name"])

print('---Turf War Stages---')
print(turfwarstage1)
print(turfwarstage2)
print()
print('---Anarchy Series Stages---')
print('Mode: ' + anarchyseriesmode)
print(anarchyseriesstage1)
print(anarchyseriesstage2)
print()
print('---Anarchy Open Stages---')
print('Mode: ' + anarchyopenmode)
print(anarchyopenstage1)
print(anarchyopenstage2)
print()
print('---X Battle Stages---')
print('Mode: ' + xbattlemode)
print(xbattlestage1)
print(xbattlestage2)
print()
print('---Salmon Run---')
print(salmonstage)
print("1: " + srweapon1)
print("2: " + srweapon2)
print("3: " + srweapon3)
print("4: " + srweapon4)