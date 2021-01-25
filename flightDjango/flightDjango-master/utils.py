import datetime
import json
import logging

import jwt


def get_logger(name=__name__):
    """
    获取一个logger，用以格式化输出信息
    :param name:
    :return:
    """
    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    # 使用StreamHandler输出到屏幕
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


'''
返回错误
'''


def return_error(code=40000, msg='error'):
    data = {
        "code": code, "data": {"msg": msg}
    }
    return json.dumps(data)


'''
token相关函数
'''


def creat_token(data):
    return jwt.encode(data, 'secret', algorithm='HS256')


def confim_token(token):
    try:
        jwt.decode(token, 'secret', algorithms=['HS256'])
        return True
    except:
        get_logger("token").info("token验证失败")
        return False


def get_info_from_token(data):
    '''

    :param data: token
    :return:
    '''
    if confim_token(data):
        return jwt.decode(data, 'secret', algorithms=['HS256'])
    else:
        return


def location_all():
    '''

    :return: 以json格式返回location.json文件的数据
    '''
    f = open(
        "D:/WorkAll/Python/flight/location.json")
    data = json.load(f)
    return data


def deletelocation(id):
    """

    :param id: location的id
    :return:
    """
    try:
        flag = False
        alllocation = location_all()
        for i, val in enumerate(alllocation['data']):
            if val['id'] == id:
                alllocation['data'].pop(i)
                flag = True
                break
        if flag == False:
            return False
        with open("D:/WorkAll/Python/flight/location.json", 'w') as f:
            json.dump(alllocation, f, ensure_ascii=False)

        return True
    except Exception as e:
        get_logger("utils").info(e)
        return False


def modifyLocation(id, name):
    '''

    :param id: location的id
    :param name: 要修改的location name
    :return:
    '''
    try:
        alllocation = location_all()
        for i in alllocation['data']:
            if i['id'] == id:
                i['name'] = name
        with open("D:/WorkAll/Python/flight/location.json", 'w') as f:
            json.dump(alllocation, f, ensure_ascii=False)
        return True
    except Exception as e:
        get_logger("utils").info(e)
        return False


def add_location(name):
    try:
        alllocation = location_all()
        sorted(alllocation['data'], key=lambda i: i['id'])
        adid = alllocation['data'][-1]['id'] + 1
        alllocation['data'].append({'id': adid, "name": name})
        with open("D:/WorkAll/Python/flight/location.json", 'w') as f:
            json.dump(alllocation, f, ensure_ascii=False)
        return True
    except Exception as e:
        get_logger("utils").info(e)
        return False


def get_location_name(id):
    '''

    :param id: loction的id
    :return: 对应的name
    '''
    all_location = location_all()['data']
    for i in all_location:
        if i['id'] == id:
            return i['name']
    return "未查到此地"

def get_location_id(name):
    '''

    :param id: loction的id
    :return: 对应的name
    '''
    all_location = location_all()['data']
    for i in all_location:
        if i['name'] == name:
            return i['id']
    return -1

def airline_all():
    '''

    :return: airline.json文件的json格式数据
    '''
    f = open(
        "D:/WorkAll/Python/flight/airline.json")
    data = json.load(f)
    return data


def get_airline_name(id):
    '''

    :param id: airline 的id
    :return: 对应的name
    '''
    all_airline = airline_all()['data']
    for i in all_airline:
        if i['id'] == id:
            return i['name']
    return "未查到此航空公司"


def add_airline(name, identifier):
    '''

    :param name:
    :param id:
    :param identifier:
    :return:
    '''
    try:
        all_airline = airline_all()
        sorted(all_airline['data'], key=lambda i: i['id'])
        adid = all_airline['data'][-1]['id'] + 1
        all_airline['data'].append(
            {"id": adid, "name": name, "identifier": identifier})
        with open("D:/WorkAll/Python/flight/airline.json", 'w') as f:
            json.dump(all_airline, f, ensure_ascii=False)
        return True
    except:
        return False


def sort_airline():
    all_airline = airline_all()
    all_airline['data'].sort(key=lambda x: x["id"])
    with open("D:/WorkAll/Python/flight/airline.json", 'w') as f:
        json.dump(all_airline, f, ensure_ascii=False)


def modifyAirline(id, name, identifier):
    try:
        data = airline_all()
        for i in data['data']:
            if i['id'] == id:
                i['name'] = name
                i['identifier'] = identifier
                break
        with open("D:/WorkAll/Python/flight/airline.json", 'w') as f:
            json.dump(data, f, ensure_ascii=False)
        return True
    except:
        return False


def deleteAirline(id):
    try:
        flag = False
        allairline = airline_all()
        for i, val in enumerate(allairline['data']):
            if val['id'] == id:
                allairline['data'].pop(i)
                flag = True
                break
        if flag == False:
            return False
        with open("D:/WorkAll/Python/flight/airline.json", 'w') as f:
            json.dump(allairline, f, ensure_ascii=False)
        return True
    except Exception as e:
        get_logger("utils").info(e)
        return False


def comparetime(time1, time2):
    # time1 = data1['startTime']
    # time2 = data2['startTime']
    if datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M') < (datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M')):
        return True
    return False


def quicksort_starttime_asc(array):
    """
    快排升序
    :param array:
    :return:
    """
    return array if len(array) <= 1 else quicksort_starttime_asc([item for item in array[1:] if
                                                         datetime.datetime.strptime(item['startTime'],
                                                                                    '%Y-%m-%d %H:%M') <= datetime.datetime.strptime(
                                                             array[0]['startTime'], '%Y-%m-%d %H:%M')]) + [
                                             array[0]] + quicksort_starttime_asc(
        [item for item in array[1:] if
         datetime.datetime.strptime(item['startTime'], '%Y-%m-%d %H:%M') > datetime.datetime.strptime(
             array[0]['startTime'], '%Y-%m-%d %H:%M')])


def quicksort_starttime_des(array):
    '''
    :param array:
    :return:
    '''
    return array if len(array) <= 1 else quicksort_starttime_des([item for item in array[1:] if
                                                         datetime.datetime.strptime(item['startTime'],
                                                                                    '%Y-%m-%d %H:%M') >= datetime.datetime.strptime(
                                                             array[0]['startTime'], '%Y-%m-%d %H:%M')]) + [
                                             array[0]] + quicksort_starttime_des(
        [item for item in array[1:] if
         datetime.datetime.strptime(item['startTime'], '%Y-%m-%d %H:%M') < datetime.datetime.strptime(
             array[0]['startTime'], '%Y-%m-%d %H:%M')])
def quicksort_endtime_asc(array):
    """
    快排升序
    :param array:
    :return:
    """
    return array if len(array) <= 1 else quicksort_endtime_asc([item for item in array[1:] if
                                                         datetime.datetime.strptime(item['startTime'],
                                                                                    '%Y-%m-%d %H:%M') <= datetime.datetime.strptime(
                                                             array[0]['startTime'], '%Y-%m-%d %H:%M')]) + [
                                             array[0]] + quicksort_endtime_asc(
        [item for item in array[1:] if
         datetime.datetime.strptime(item['startTime'], '%Y-%m-%d %H:%M') > datetime.datetime.strptime(
             array[0]['startTime'], '%Y-%m-%d %H:%M')])


def quicksort_endtime_des(array):
    '''
    :param array:
    :return:
    '''
    return array if len(array) <= 1 else quicksort_endtime_des([item for item in array[1:] if datetime.datetime.strptime(item['startTime'],'%Y-%m-%d %H:%M') >= datetime.datetime.strptime(array[0]['startTime'], '%Y-%m-%d %H:%M')]) \
                                         + [array[0]] \
                                         + quicksort_endtime_des([item for item in array[1:] if datetime.datetime.strptime(item['startTime'], '%Y-%m-%d %H:%M') < datetime.datetime.strptime(array[0]['startTime'], '%Y-%m-%d %H:%M')])
def flightsorttool(list,order,column):
    """
    暂时只做了对于出发时间和结束时间的快排（其他排序无必要）
    :param list:
    :param order:
    :param column:
    :return:
    """
    if order == 'descending' and column =='startTime':
        return quicksort_starttime_des(list)
    elif order == 'ascending' and column =='startTime':
        return quicksort_starttime_asc(list)
    elif order == 'descending' and column =='endTime':
        return quicksort_endtime_des(list)
    elif order == 'ascending' and column =='endTime':
        return quicksort_endtime_asc(list)
    return list
def getairId_from_name(name):
    if name:
        allair = airline_all()['data']
        for i in allair:
            if i['name'] == name:
                return i['id']
    return -1
def getlocationId_from_name(name):
    if name:
        locationall = location_all()['data']
        for i in locationall:
            if i['name'] == name:
                return i['id']
    return -1

# print(get_location_id('北京'))