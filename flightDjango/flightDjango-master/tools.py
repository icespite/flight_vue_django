'''
@Author       : IceSpite
@Date         : 2020-03-20 23:22:16
@LastEditTime : 2020-03-25 13:30:24
'''
import json
from datetime import datetime

import user.inform
import utils

stop = {}
stop['stop'] = []
idd = 4


def locationsasdasda():
    f = open("D:/WorkAll/Python/flight/location.json")
    data = json.load(f)
    return data


def airline_all():
    f = open("D:/WorkAll/Python/flight/airline.json")
    data = json.load(f)
    return data


airlines = airline_all()
locati = locationsasdasda()['data']

airid = 3
def ifinairline(name):
    global airid,airlines
    for i in airlines['data']:
        if i['name'] == name:
            return True
    airlines['data'].append({
        "id":airid,
        'name':name,
        'identifier':''
    })
    airid+=1
    return False


def location_all():
    f = open("D:/WorkAll/Python/flight/flylog.json")
    data = json.load(f)
    return data


locations = location_all()

for i in locations['data']:
    for j in airlines['data']:
        if i['airId'] == j['name']:
            i['airId'] = j['id']
            break


