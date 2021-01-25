import requests

# key = 'f247cdb592eb43ebac6ccd27f796e2d2'

def getlocation(addr):
    url = 'http://api.map.baidu.com/geocoder?address=%s&output=json&key=f247cdb592eb43ebac6ccd27f796e2d2' % (addr)
    res = requests.get(url)
    data = res.json()
    return data['result']['location']


def distance(a1, a2):
    loc1, loc2 = getlocation(a1), getlocation(a2)
    latdiff = loc1['lat'] - loc2['lat']
    lngdiff = loc1['lng'] - loc2['lng']
    miles = ((69.1 * latdiff) ** 2 + (53.0 * lngdiff) ** 2) ** .5
    return miles * 1.6092953


if __name__ == '__main__':
    print(distance('庆云', '长春'))
