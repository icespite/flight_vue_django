"""
@Author       : IceSpite
@Date         : 2020-03-18 14:42:33
@LastEditTime : 2020-03-25 13:53:33
"""
import datetime
import json

import utils


def flylog_all():
    f = open("D:/WorkAll/Python/flight/flylog.json")
    data = json.load(f)
    return data


def write_to_flylog(data):
    if data:
        with open("D:/WorkAll/Python/flight/flylog.json", "w") as f:
            json.dump(data, f, ensure_ascii=False)


def search_flylog_by_flightNumber(flight_number):
    all_flylog = flylog_all()["data"]
    data = []
    for i in all_flylog:
        if i["flightNumber"] == flight_number:
            i["startlocationId"] = utils.get_location_name(i["startlocationId"])
            i["endlocationId"] = utils.get_location_name(i["endlocationId"])
            for item in i["stop"]:
                item["location"] = utils.get_location_name(item["location"])
            i["airId"] = utils.get_airline_name(i["airId"])
            # print(i)
            data.append(i)
    return data


def search_flylog_by_flightNumber_noreplace(flight_number):
    all_flylog = flylog_all()["data"]
    data = []
    for i in all_flylog:
        if i["flightNumber"] == flight_number:
            data.append(i)
    return data


def endProcess(data):
    data["startlocationId"] = utils.get_location_name(data["startlocationId"])
    data["endlocationId"] = utils.get_location_name(data["endlocationId"])
    for item in data["stop"]:
        item["location"] = utils.get_location_name(item["location"])
    data["airId"] = utils.get_airline_name(data["airId"])
    return data


def search_flylog_by_Id(id):
    """
    :param id:
    :return: 一条flylog数据
    """
    all_flylog = flylog_all()["data"]
    if all_flylog[id]["id"] == id:
        return endProcess(all_flylog[id])

    for ind, value in enumerate(all_flylog):
        if value['id'] == id:
            return endProcess(value)
    # left = id - 1
    # right = id + 1
    # while left >= 0 or right <= len(all_flylog):
    #     if all_flylog[left]["id"] == id:
    #         return endProcess(all_flylog[left])
    #     if all_flylog[right]["id"] == id:
    #         return endProcess(all_flylog[right])
    #     left -= 1
    #     right += 1
    return None


def if_sameday(time1, time2):
    """
    :param time1: time1与2均为str
    :param time2:
    :return:
    """
    try:
        t1 = datetime.datetime.strptime(time1, "%Y-%m-%d")
    except:
        t1 = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M")
    t2 = datetime.datetime.strptime(time2, "%Y-%m-%d %H:%M")
    if t1.day == t2.day and t1.month == t2.month:
        if (
                t1.day == datetime.datetime.now().day
                and t1.month == datetime.datetime.now().month
        ):
            if (t2 - datetime.datetime.now()).seconds > 0:
                return True
            else:
                return False
        else:
            return True
    return False


def search_flylog_by_locations_and_time(start, end, time):
    all_flylog = flylog_all()["data"]
    res = []
    for i in all_flylog:
        if (
                utils.get_location_name(i["startlocationId"]) == start
                and utils.get_location_name(i["endlocationId"]) == end
                and if_sameday(time, i["startTime"])
                # and i['condition'] == 1
        ):
            # 把id换成地名字
            all_location = utils.location_all()["data"]
            i["startlocationId"] = utils.get_location_name(i["startlocationId"])
            i["endlocationId"] = utils.get_location_name(i["endlocationId"])
            for item in i["stop"]:
                item["location"] = utils.get_location_name(item["location"])
            i["airId"] = utils.get_airline_name(i["airId"])
            res.append(i)
    return res


def ticketdecrease(flylogId):
    """
    没有判断是否会出现小于零的情况
    :param flylogId:
    :return:
    """
    all_flylog = flylog_all()
    reallocation = flylogId
    if all_flylog["data"][flylogId]["id"] != flylogId:
        left = flylogId - 1
        right = flylogId + 1
        while left >= 0 or right <= len(all_flylog):
            if all_flylog["data"][left]["id"] == flylogId:
                reallocation = left
                break
            if all_flylog["data"][right]["id"] == flylogId:
                reallocation = right
                break
            left -= 1
            right += 1
    all_flylog["data"][reallocation]["ticket"] -= 1
    write_to_flylog(all_flylog)


def modifycondition(id, condition=0):
    """
    :param int id: flylog的id
    :param int condition: 0代表取消 1代表正常 2代表延误
    :return:
    """

    all_flylog = flylog_all()
    if len(all_flylog["data"]) < id or id <= 0:
        return (40000, "没有该id", "nothing")
    index = -1
    if all_flylog["data"][id]["id"] == id:
        index = id
    else:
        for ind, value in enumerate(all_flylog['data']):
            if value['id'] == id:
                index = ind
                break
        # left = id - 1
        # right = id + 1
        # while left >= 0 or right <= len(all_flylog):
        #     if all_flylog["data"][left]["id"] == id:
        #         index = left
        #     if all_flylog["data"][right]["id"] == id:
        #         index = right
        #     left -= 1
        #     right += 1
    if index != -1:
        all_flylog["data"][index]["condition"] = condition
    write_to_flylog(all_flylog)
    tuijian = search_flylog_by_locations_and_time(
        utils.get_location_name(all_flylog["data"][index]["startlocationId"]),
        utils.get_location_name(all_flylog["data"][index]["endlocationId"]),
        datetime.datetime.strptime(
            all_flylog["data"][index]["startTime"], "%Y-%m-%d %H:%M"
        ).strftime("%Y-%m-%d"),
    )
    msg = ''
    if tuijian:
        for i in utils.quicksort_endtime_asc(tuijian):
            if datetime.datetime.strptime(
                    i["startTime"], "%Y-%m-%d %H:%M"
            ) == datetime.datetime.strptime(
                all_flylog["data"][index]["startTime"], "%Y-%m-%d %H:%M"
            ):
                if all_flylog["data"][index]["flightNumber"] != i["flightNumber"]:
                    msg = msg + i["flightNumber"] + ','
            elif datetime.datetime.strptime(
                    i["startTime"], "%Y-%m-%d %H:%M"
            ) > datetime.datetime.strptime(
                all_flylog["data"][index]["startTime"], "%Y-%m-%d %H:%M"
            ):
                msg = i["flightNumber"]
                break
    if msg == '':
        msg = '暂无'
    return (20000, "推荐航班：" + msg, all_flylog["data"][index]["flightNumber"])


def modifyflylogprocess(data):
    """
    1. 判断时间 2.计算预估时间 3. 余票数量不能是负数 4. id都换成对应id
    :param data:
    :return:
    """
    try:
        if data["ticket"] < 0 or data["price"] < 0:
            return (40000, "余票或价格不能为负数")
        data["startlocationId"] = utils.getlocationId_from_name(data["startlocationId"])
        data["endlocationId"] = utils.getlocationId_from_name(data["endlocationId"])
        data["airId"] = utils.getairId_from_name(data["airId"])
        if len(data["stop"]) > 0:
            for i in data["stop"]:
                i["location"] = utils.getlocationId_from_name(i["location"])
        starttime = datetime.datetime.strptime(data["startTime"], "%Y-%m-%d %H:%M")
        endtime = datetime.datetime.strptime(data["endTime"], "%Y-%m-%d %H:%M")
        if starttime > endtime:
            return (40000, "到达时间不能早于出发时间")
        if (endtime - starttime).days > 1:
            data["estimateTime"] = datetime.datetime.strptime(
                str(endtime - starttime), "%d days, %H:%M:%S"
            ).strftime("%d:%H:%M")
        elif (endtime - starttime).days == 1:
            data["estimateTime"] = datetime.datetime.strptime(
                str(endtime - starttime), "%d day, %H:%M:%S"
            ).strftime("%d:%H:%M")

        else:
            data["estimateTime"] = datetime.datetime.strptime(
                str(endtime - starttime), "%H:%M:%S"
            ).strftime("00:%H:%M")
        all = flylog_all()
        for index, value in enumerate(all["data"]):
            if value["id"] == data["id"]:
                all["data"][index] = data
                # print(all["data"][index])
        write_to_flylog(all)
        return (20000, "success")
    except Exception as e:
        print(e)
        return (40000, "未知错误")


def deleteflylog(id):
    all_flylog = flylog_all()
    for index, value in enumerate(all_flylog['data']):
        if value['id'] == id:
            all_flylog['data'].pop(index)
            break
    write_to_flylog(all_flylog)

def flylogticketadd(flylogid):
    all_flylog = flylog_all()
    for index, value in enumerate(all_flylog['data']):
        if value['id'] == flylogid:
            value['ticket']+=1
            break
    write_to_flylog(all_flylog)

def addflylog(data):
    all_flylog = flylog_all()['data']
    maxid = -1
    for i in all_flylog:
        if i['id'] > maxid:
            maxid = i['id']
    maxid += 1
    data['id'] = maxid
    try:
        if data["ticket"] < 0 or data["price"] < 0:
            return (40000, "余票或价格不能为负数")
        data["startlocationId"] = utils.getlocationId_from_name(data["startlocationId"])
        data["endlocationId"] = utils.getlocationId_from_name(data["endlocationId"])
        data["airId"] = utils.getairId_from_name(data["airId"])
        if len(data["stop"]) > 0:
            for i in data["stop"]:
                i["location"] = utils.getlocationId_from_name(i["location"])
        starttime = datetime.datetime.strptime(data["startTime"], "%Y-%m-%d %H:%M")
        endtime = datetime.datetime.strptime(data["endTime"], "%Y-%m-%d %H:%M")
        if starttime > endtime:
            return (40000, "到达时间不能早于出发时间")
        if (endtime - starttime).days > 1:
            data["estimateTime"] = datetime.datetime.strptime(
                str(endtime - starttime), "%d days, %H:%M:%S"
            ).strftime("%d:%H:%M")
        elif (endtime - starttime).days == 1:
            data["estimateTime"] = datetime.datetime.strptime(
                str(endtime - starttime), "%d day, %H:%M:%S"
            ).strftime("%d:%H:%M")

        else:
            data["estimateTime"] = datetime.datetime.strptime(
                str(endtime - starttime), "%H:%M:%S"
            ).strftime("00:%H:%M")
        all = flylog_all()
        all['data'].append(data)
        write_to_flylog(all)
        return (20000, "success")
    except Exception as e:
        print(e)
        return (40000, "未知错误")


# modifycondition(372,2)
# print(search_flylog_by_Id(372))
