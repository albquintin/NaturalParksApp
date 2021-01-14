import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8069
DB = 'odoo'
USER = 'admin'
PASS = 'admin'

def json_rpc_car_read(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc_car_read(url, "call", {"service": service, "method": method, "args": args})

url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

car_id = call(url, "object", "execute", DB, uid, PASS, 'naturalparks.car', 'read', [1])
print("Reading car 1...", car_id)