import urllib2
import json
import time
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:3306')

db = client.my_database

def remove_dot_key(obj):
    for key in obj.keys():
        new_key = key.replace(".","_")
        if new_key != key:
            obj[new_key] = obj[key]
            del obj[key]
    return obj

while (true) {
    time.sleep(60)
    data = json.loads(urllib2.urlopen("http://localhost:4000/api/v1.3/subcontainers/docker").read(), object_hook=remove_dot_key) 
    db.results.insert_many(data)
    
}

