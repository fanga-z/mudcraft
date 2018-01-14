from urllib.request import urlopen
from pathlib import Path
from datetime import date
import json
import os
import pickle

cache = "weather.pkl"

def _shouldUpdateCache():
    global cache
    if Path(cache).exists():
        result = os.stat(cache)
        modify_time = date.fromtimestamp(result.st_mtime)
        dt = date.today() - modify_time
        if dt.days > 0:
            return True
        return False
    else:
        return True

def _to_cache():
    global cache
    url = "http://www.sojson.com/open/api/weather/json.shtml?city=%E5%8C%97%E4%BA%AC"
    info = {"city":"虚空", "data":{"wendu":10, "pm25":0,"quality":"好"}}
    with urlopen(url) as response:
        str = ""
        for line in response:
            str = str + line.decode('utf-8')
        info = json.loads(str,encoding='utf-8')

    pickle_file = open(cache, 'bw')
    pickle.dump(info, pickle_file)
    pickle_file.close()

    return info

def _from_cache():
    global cache
    pickle_file = open(cache, 'br')
    info = pickle.load(pickle_file)
    pickle_file.close()
    return info

def get_weather():
    #url = "http://way.weatherdt.com/tianyi/grid_fd_observe?serialNo=0001&appkey=b794065a61862a7b26f9650c188f933b"
    #加上本地缓存
    if _shouldUpdateCache(): 
        info = _to_cache() 
    else:
        info = _from_cache()    
    return info
    