import json
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import manager.flylog

# Create your views here.
from login.views import get_info_from_token
from user.dij import dij
from user.inform import (
    confirm_inform_to_json,
    get_allinform_from_json,
    get_inform_from_json,
)
import utils
import user.buy
from user.buy import buyWait

log = utils.get_logger("user.view")


def get_inform(request):
    token = request.headers.get("X-Token")
    info = get_info_from_token(token)
    try:
        res = get_allinform_from_json(info["userId"])
        data = {"code": 20000, "data": res}
        return HttpResponse(json.dumps(data))
    except ValueError as v:
        return HttpResponse(utils.return_error(code=40000, msg="文件打开失败，请等待管理人员排查"))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def confirm_inform(request):
    token = request.headers.get("X-Token")
    info = get_info_from_token(token)
    try:
        if not info:
            raise ValueError
        if (
                datetime.datetime.strptime(info["time"], "%Y-%m-%d %H:%M:%S.%f")
                - datetime.datetime.strptime(
            str(datetime.datetime.now()), "%Y-%m-%d %H:%M:%S.%f"
        )
        ).seconds > 60 * 60 * 2:
            data = {"code": 50014, "data": {"msg": "token已过期，请重新登录"}}
            print("token过期")
            return HttpResponse(json.dumps(data))
        else:
            confirm_inform_to_json(int(request.GET.get("id")))
            data = {"code": 20000, "data": {"msg": "success"}}
            return HttpResponse(json.dumps(data))
    except ValueError as v:
        return HttpResponse(utils.return_error(code=50008, msg="token不正确"))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


"""
根据出发地和目的的查询航班
"""


def search_flights(request):
    try:
        res = json.loads(request.body)
        timeY = res["time"]
        time = datetime.datetime.strptime(res["time"], "%Y-%m-%d")
        flylogs = manager.flylog.search_flylog_by_locations_and_time(
            res["start"], res["end"], timeY
        )
        if flylogs:
            data = {"code": 20000, "data": flylogs}
            return HttpResponse(json.dumps(data))
        else:
            data = {"code": 20000, "data": {"msg": "未查询到该航班"}}
            return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


"""
得到所有的location
"""


def get_all_location(request):
    try:
        res = utils.location_all()
        data = {"code": 20000, "data": res}
        return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def view_serch_flylog_byflightNumber(request):
    try:
        flight_number = request.GET.get("flightNumber")
        res = manager.flylog.search_flylog_by_flightNumber(flight_number)
        if not res:
            raise ValueError
        data = {"code": 20000, "data": res}
        # data["data"].append(res)
        return HttpResponse(json.dumps(data))
    except ValueError as v:
        log.error("未查询到该航班")
        data = {"code": 20000, "data": {"msg": "未查询到该航班"}}
        return HttpResponse(json.dumps(data))
    except:
        return HttpResponse(utils.return_error())


def get_all_airline(request):
    try:
        res = utils.airline_all()["data"]
        data = {"code": 20000, "data": res}
        return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def try_buy_post(request):
    try:
        token = request.headers.get("X-Token")
        info = get_info_from_token(token)
        userId = info["userId"]
        id = int(request.POST["id"])  # flylog的id
        if user.buy.cheack_if_buy(userId, id) == False:
            if user.buy.buyFlight(userId, id):
                data = {"code": 20000, "data": {"msg": "success"}}
                return HttpResponse(json.dumps(data))

        data = {"code": 20000, "data": {"msg": "您已经购买过该机票"}}
        return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def buy_wait_post(request):
    try:
        id = int(request.POST['id'])
        token = request.headers.get("X-Token")
        info = get_info_from_token(token)
        userId = info["userId"]
        if user.buy.cheack_if_buy(userId, id) == False:
            flylogid = int(request.POST["id"])  # 从表单获取
            seat = "XXX"
            buyWait(userId, flylogid, seat)
            data = {"code": 20000, "data": {"msg": "success"}}
            return HttpResponse(json.dumps(data))
        data = {"code": 20000, "data": {"msg": "您已经购买过该机票"}}
        return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def get_all_buy_info(request):
    try:
        token = request.headers.get("X-Token")
        info = get_info_from_token(token)
        userId = info["userId"]
        res = user.buy.search_buy_userid(userId)
        data = {
            "code": 20000,
            "data": res
        }
        return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def flightorder(request):
    try:
        list = json.loads(request.POST['data'])
        order = request.POST['order']
        column = request.POST['column']
        res = utils.flightsorttool(list, order, column)
        data = {
            "code": 20000,
            "data": res
        }
        return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())

def cancel_buy(request):
    try:
        id = request.POST['id']
        classify = request.POST['classify']
        user.buy.cancelbuy(int(id), classify)
        data = {
            "code": 20000,
            "data": 'success'
        }
        return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())
def searchflightless(request):
    try:
        time = request.POST['time']  # flylog的id
        classify = request.POST['classify']
        startid = utils.get_location_id(request.POST['startid'])
        endid = utils.get_location_id(request.POST['endid'])
        print(time,startid,endid,classify)
        if time and classify and startid and endid:
            res = dij(time).dij_less_money(classify, startid, endid)
            data = {
                "code": 20000,
                'data': res
            }
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse(utils.return_error())
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())