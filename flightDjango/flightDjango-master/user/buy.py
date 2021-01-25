'''
@Author: IceSpite
@Date: 2020-03-24 22:44:30
@LastEditTime: 2020-03-24 23:11:46
'''
import datetime
import json
import utils
from user.inform import addInform

log = utils.get_logger("buy.py")
from manager.flylog import flylog_all, search_flylog_by_Id, ticketdecrease, flylogticketadd


def getAllBuyData():
    '''
    @msg: 
    @param  
    @return: buy.json的json格式
    '''
    f = open("D:/WorkAll/Python/flight/buy.json")
    data = json.load(f)
    return data


def write_to_buy(data):
    with open("D:/WorkAll/Python/flight/buy.json", 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def getDoneData():
    return getAllBuyData()['data']['done']


def getWaitData():
    return getAllBuyData()['data']['wait']


def buyWait(userId, flylogid, seat='xxx'):
    try:
        flyloginfo = search_flylog_by_Id(flylogid)
        towritte = {
            "id": getMaxWaitId() + 1,
            "userId": userId,
            "flightNumber": flyloginfo['flightNumber'],
            'flylogid':flylogid,
            "time": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M"),
            "seat": seat,
            "status": 1
        }
        data = getAllBuyData()
        data['data']['MaxWaitId'] += 1
        data['data']['wait'].append(towritte)
        write_to_buy(data)
        return True
    except Exception as e:
        log.error(e)
        return False


def getMaxDoneId():
    return getAllBuyData()['data']['MaxDoneId']


def getMaxWaitId():
    return getAllBuyData()['data']['MaxWaitId']


def buyFlight(userid, flylogid):
    flyloginfo = search_flylog_by_Id(flylogid)
    if flyloginfo["ticket"] > 0:
        # 待补充
        towritte = {
            "id": getMaxDoneId() + 1,
            "userId": userid,
            "flightNumber": flyloginfo['flightNumber'],
            'flylogid': flylogid,
            "time": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M"),
            "seat": "A1",
            "status": 1
        }
        data = getAllBuyData()
        data['data']['MaxDoneId'] += 1
        data['data']['done'].append(towritte)
        write_to_buy(data)
        ticketdecrease(flylogid)
        return True
    else:
        return False


def cheack_if_buy(userId, flylogid):
    flyloginfo = search_flylog_by_Id(flylogid)
    all = getAllBuyData()['data']
    for i in all['done']:
        if i['userId'] == userId and i['flightNumber'] == flyloginfo['flightNumber']:
            return True
    for i in all['wait']:
        if i['userId'] == userId and i['flightNumber'] == flyloginfo['flightNumber']:
            return True
    return False


def search_buy_userid(userid):
    data = getAllBuyData()['data']
    result = {
        'done': [],
        'wait': []
    }
    for i in data['done']:
        if i['userId'] == userid:
            result['done'].append(i)

    for i in data['wait']:
        if i['userId'] == userid:
            result['wait'].append(i)
    return result


def change_order_status(flightnum, classify):
    all = getAllBuyData()
    for i in all['data']['done']:
        print(i)
        if  i["flightNumber"] == flightnum:
            if classify == '延误':
                i['status'] = 2
                print(i['status'] )
            elif classify == '取消':
                i['status'] = 0

    for i in all['data']['wait']:
        if  i["flightNumber"] == flightnum:
            if classify == '延误':
                i['status'] = 2
            elif classify == '取消':
                i['status'] = 0
    write_to_buy(all)


def sortbytime(array):
    return array if len(array) <= 1 else sortbytime([item for item in array[1:] if
                                                     datetime.datetime.strptime(item['time'],
                                                                                '%Y-%m-%d %H:%M') <= datetime.datetime.strptime(
                                                         array[0]['time'], '%Y-%m-%d %H:%M')]) + [
                                             array[0]] + sortbytime(
        [item for item in array[1:] if
         datetime.datetime.strptime(item['time'], '%Y-%m-%d %H:%M') > datetime.datetime.strptime(
             array[0]['time'], '%Y-%m-%d %H:%M')])


def cancelbuy(id, classify):
    # 接受总的id，classify区分是done还是wait    记得退票后抢票自动购买
    all = getAllBuyData()
    if classify == 'wait':
        for index, value in enumerate(all['data']['wait']):
            if value['id'] == id:
                all['data']['wait'].pop(index)
    if classify == 'done':
        flylogid =1
        flag = True
        for index, value in enumerate(all['data']['done']):
            if value['id'] == id:
                flylogid = value['flylogid']
                all['data']['wait'] = sortbytime(all['data']['wait'])
                for i, j in enumerate(all['data']['wait']):
                    if j['flylogid'] == value['flylogid']:
                        flag = False
                        towritte = {
                            "id": getMaxDoneId() + 1,
                            "userId": j["userId"],
                            "flightNumber": value['flightNumber'],
                            'flylogid': value['flylogid'] ,
                            "time": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M"),
                            "seat": "A1",
                            "status": 1
                        }
                        userid = j["userId"]
                        flight =  value['flightNumber']
                        addInform(userid, '您预定的' + flight + '购买成功')
                        all['data']['wait'].pop(i)
                        all['data']['done'].append(towritte)
                        all['data']["MaxDoneId"] += 1
                        break
                all['data']['done'].pop(index)
                break
        if flag:
            flylogticketadd(flylogid)
    write_to_buy(all)


def changewaittobuy(flightnum):
    '''
    TODO:顾客退票时使用
    :param flightnum:
    :return:
    '''
    all = getAllBuyData()
    waitqueue = []
    all['data']['wait'] = sortbytime(all['data']['wait'])

    for index, value in enumerate(all['data']['wait']):
        if value['flightNumber'] == flightnum:
            all['data']['wait'].pop(index)

            towritte = {
                "id": getMaxDoneId() + 1,
                "userId": value['userId'],
                "flightNumber": flightnum,
                "time": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M"),
                "seat": "A1",
                "status": 1
            }
            all['data']['done'].append(towritte)
            all['data']['MaxDoneId'] += 1

            addInform(value['userId'], '您预订的' + flightnum + '购买成功')
            break
    write_to_buy(all)


# changewaittobuy('WU11111')
# cancelbuy(4,'done')
# print(sortbytime(getAllBuyData()['data']['wait']))
# change_order_status('SU1111', '延误')
# cancelbuy(5,'done')