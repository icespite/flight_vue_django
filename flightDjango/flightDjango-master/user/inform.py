import datetime
import json
import time
from collections import defaultdict
import logging

# from user.buy import getAllBuyData

logging.basicConfig(level=logging.INFO)
STATUE = True


def informAll():
    f = open(
        "D:/WorkAll/Python/flight/inform.json")
    data = json.load(f)
    return data


def writetoinform(data):
    with open("D:/WorkAll/Python/flight/inform.json", 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def get_allinform_from_json(user_id):
    '''
    @description: 
    @param user_id 用户id 
    @return: 
    '''
    global STATUE
    while STATUE != True:
        time.sleep(0.3)
    data = informAll()
    re = {'item': []}
    for i in data['data']:
        if i['userId'] == user_id:
            re['item'].append(i)
    return re


def get_inform_from_json(user_id):
    '''
    @description: 
    @param user_id 用户id 
    @return: 
    '''
    global STATUE
    while STATUE != True:
        time.sleep(0.3)
    data = informAll()
    re = {'item': []}
    for i in data['data']:
        if i['userId'] == user_id and i['haveConfirm'] == False:
            re['item'].append(i)
    return re


def confirm_inform_to_json(id):
    global STATUE
    data = informAll()
    # logging.INFO(data)
    STATUE = False
    for i in data['data']:
        if id == i['id']:
            i['haveConfirm'] = True
    with open("D:/WorkAll/Python/flight/inform.json", 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    STATUE = True


def addInform(id, msg):
    """

    :param id: 用户id
    :param msg:
    :return:
    """
    allinform = informAll()
    data = {
        "id": len(allinform['data']) + 1,
        "userId": id,
        "haveConfirm": False,
        "msg": msg,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    allinform['data'].append(data)
    writetoinform(allinform)


