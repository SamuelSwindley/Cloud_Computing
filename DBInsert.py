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

while (True) :
    time.sleep(60)
    data1 = json.loads(urllib2.urlopen("http://localhost:4000/api/v1.3/subcontainers/docker/65df8e9g4brt65n1tntb6sd5g18t74m1hdghjngh65f4g894641hd68h4tn1f4ng").read(), object_hook=remove_dot_key) 
    data2 = json.loads(urllib2.urlopen("http://localhost:4000/api/v1.3/subcontainers/docker/2x1c54ht5uyjkyu78t48gs632df1cf65b1rj8yu4k9u87l9y8he65g1fg32h1tr6").read(), object_hook=remove_dot_key) 
    db.container1.insert_many(data1) 
    db.container2.insert_many(data2)


