import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import utils
from manager import flylog
from manager.flylog import deleteflylog
from user.buy import getAllBuyData, changewaittobuy, change_order_status
from user.dij import dij
from user.inform import addInform

log = utils.get_logger("manger.view")


def modietfy_location(request):
    try:
        id = int(request.POST['id'])
        name = request.POST['name']
        if name and id:
            assert utils.modifyLocation(id, name)
            data = {
                "code": 20000,
                "msg": "success"
            }
            return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def add_location(request):
    try:
        name = request.POST['name']
        if name:
            assert utils.add_location(name)
            data = {
                "code": 20000,
                "msg": "success"
            }
            return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def delete_location(request):
    try:
        id = int(request.POST['id'])
        if id:
            assert utils.deletelocation(id)
            data = {
                "code": 20000,
                "msg": "success"
            }
            return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def delete_airline(request):
    try:
        id = int(request.POST['id'])
        if id:
            assert utils.deleteAirline(id)
            data = {
                "code": 20000,
                "msg": "success"
            }
            return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def modify_airline(request):
    try:
        id = int(request.POST['id'])
        name = request.POST['name']
        identify = request.POST['identifier']
        if name and id and identify:
            assert utils.modifyAirline(id, name, identify)
            data = {
                "code": 20000,
                "msg": "success"
            }
            return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def add_airline(request):
    try:
        name = request.POST['name']
        identify = request.POST['identifier']
        if name and id and identify:
            assert utils.add_airline(name, identify)
            data = {
                "code": 20000,
                "msg": "success"
            }
            return HttpResponse(json.dumps(data))
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def modifyFlight(request):
    try:
        list = json.loads(request.POST['list'])
        list['price'] = int(list['price'])
        list['ticket'] = int(list['ticket'])
        if list:
            code, msg = flylog.modifyflylogprocess(list)
            data = {
                "code": code,
                "msg": msg
            }
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse(utils.return_error())
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())


def addFlight(request):
    try:
        list = json.loads(request.POST['list'])
        list['price'] = int(list['price'])
        list['ticket'] = int(list['ticket'])
        print(list)
        if list:
            code, msg = flylog.addflylog(list)
            data = {
                "code": code,
                "msg": msg
            }
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse(utils.return_error())
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())
def deleteFlight(request):
    try:
        list = json.loads(request.POST['list'])
        if list:
            id = list['id']
            deleteflylog(id)
            flylog.modifycondition(id, 0)
            data = {
                "code": 20000,
                "msg": 'success'
            }
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse(utils.return_error())
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())
def cancelflight(request):
    try:
        id = int(request.POST['id'])  # flylog的id
        classify = request.POST['classify']
        condi = 1
        if id:
            if classify == '"取消"':
                condi = 0
            elif classify == '"延误"':
                condi = 2
            else:
                return HttpResponse(utils.return_error())
            code, msg, flightnum = flylog.modifycondition(id, condi)

            if classify == '"取消"':
                change_order_status(flightnum, '取消')
            elif classify == '"延误"':
                change_order_status(flightnum, '延误')


            data = {
                "code": code,
                "msg": msg
            }
            if code == 20000:
                allwait = []
                allbuy = getAllBuyData()
                for i in allbuy['data']['done']:
                    if i['flightNumber'] == flightnum:
                        addInform(i['userId'], '您购买的' + flightnum + '已被' + classify + ',' + msg)
                        allwait.append(i)
                for i in allbuy['data']['wait']:
                    if i['flightNumber'] == flightnum:
                        addInform(i['userId'], '您预定的' + flightnum + '已被' + classify + ',' + msg)
                        allwait.append(i)
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse(utils.return_error())
    except Exception as e:
        log.error(e)
        return HttpResponse(utils.return_error())



