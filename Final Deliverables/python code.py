import wiotp.sdk.device
import time
import random
import collections.abc

try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

myConfig = {
"identity": {
"orgId": "gx76pd",
"typeId": "SmartBin",
"deviceId":"bin-1"
},
"auth": {
"token": "ZeskE9*BHtQSqNlICL"
}
}
def myCommandCallback (cmd):
 print ("Message received from IBM IoT Platform: %s" % cmd.data['command'])
m=cmd.data['command']
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
def pub (data):
 client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0,
onPublish=None)
print ("Published data Successfully: %s", myData)
while True:
 myData={'name': 'Bin1', 'lat': 13.092677, 'lon': 80.188314}
pub (myData)
time.sleep (3)
client.commandCallback = myCommandCallback
client.disconnect ()
