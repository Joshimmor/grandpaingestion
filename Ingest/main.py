from m3u_parser import M3uParser
from dataclasses import dataclass
import json
from collections import namedtuple
from json import JSONEncoder
import sqlite3


    
class tvg:
    id: str
    name: str
    url: str  
class country:
    code:str
    name:str
class language:
    code: str
    name: str
@dataclass
class channel:
    name: str
    logo: str 
    url: str
    category: str
    tvg: tvg
    country :country 
    language:language
    status: str
    live: bool
def database(multiple_columns):
    try:
        conn = sqlite3.connect("C:\\Users\\Joshua\\source\\repos\\tv\\InstagramEcom\\prisma\\dev.db")
        cursor = conn.cursor()
        #cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for i in multiple_columns:
            cursor.execute("UPDATE channel SET link = ?, artwork = ? WHERE channelName = ?", (i[0],i[1],i[2]))
        print('INFO: Command executed successfully')
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
def customChannelDecoder(channel):
    return namedtuple('X', channel.keys())(*channel.values())


if __name__ == "__main__":
    url = "../Data/Playlist.m3u"
    useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    parser = M3uParser(timeout=5, useragent=useragent)
    # Parse the m3u file
    parser.parse_m3u(url)
    channelArray = []
    for i in parser.get_list():
        channelArray.append((i['url'],i['logo'],i['name']))
    database(channelArray)