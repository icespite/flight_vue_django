import datetime
import json
import re

from django.http import HttpResponse

import utils

log = utils.get_logger("middleware")
try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


def if_manageUrl(current_path):
    manage_menu = ["/manage/."]
    for manage_url in manage_menu:
        ret = re.match(manage_url, current_path)
        if ret:
            return True
    return False


class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        current_path = request.path_info
        valid_menu = ["/api/.*"]  # 如果不设置白名单，admin的url也会被判为无权限，而且不需要验证的函数少， 先设置白名单，
        # 如果用户输入的url在白名单中就会return None
        for valid_url in valid_menu:
            ret = re.match(valid_url, current_path)  # 注意
            if ret:
                return None

        token = request.headers.get('X-Token')
        info = utils.get_info_from_token(token)
        try:
            if not info:
                raise ValueError
            if (datetime.datetime.strptime(info['time'], "%Y-%m-%d %H:%M:%S.%f") - datetime.datetime.strptime(
                    str(datetime.datetime.now()), "%Y-%m-%d %H:%M:%S.%f")).seconds > 60 * 60 * 2:
                data = {"code": 50014, "data": {"msg": "token已过期，请重新登录"}}
                return HttpResponse(json.dumps(data))
            if if_manageUrl(current_path):
                if info['role'] != 'admin':
                    return HttpResponse(utils.return_error(code=40000, msg="权限不足"))
            return None
        except ValueError as v:
            return HttpResponse(utils.return_error(code=50008, msg="token验证未通过"))
        except Exception as e:
            log.error(e)
            return HttpResponse(utils.return_error())

    def process_response(self, request, response):
        return response
