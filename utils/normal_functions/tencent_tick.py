import requests

from utils.normal_functions.TickClass import Tick


def tick_price(code):
    response = requests.get(f"http://qt.gtimg.cn/q={code},money.api").text
    info = []
    data = str(response).split(';')
    for item in data:
        _dict = {}
        if len(item) > 2:
            item_part = str(item).replace("\n", "").split('~')
            # print(item_part)
            _dict["symbol"] = item_part[2]
            _dict["name"] = item_part[1]
            _dict["open"] = float(item_part[5])
            _dict["yesterday_close"] = float(item_part[4])
            _dict["last"] = float(item_part[3])
            _dict["high"] = float(item_part[33])
            _dict["low"] = float(item_part[34])
            _dict["timestamp"] = item_part[30]
            info.append(_dict)
    # print(info)
    return info
