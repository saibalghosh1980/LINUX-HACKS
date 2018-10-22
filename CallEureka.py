import requests
import json
import pprint

allJson = []
headers = {
    'accept': "application/json",
    'cache-control': "no-cache"
}
response = requests.get(
    'http://gboxfdockprd001.uk.oup.com:8761/eureka/apps', headers=headers)
data = response.json()
for majorkey, subdict in data["applications"].items():
    # print(majorkey)
    if majorkey == 'application':
        # print(subdict[0]["name"])
        for item in subdict:
            #print(item["name"])
            data = {}
            data['name'] = ''.join(['prod-',item["name"]])
            data['scheme'] = "http"
            data['host'] = "gboxfdockprd001.uk.oup.com"
            data['port'] = 10080
            data['path'] = ''.join(["/",item["name"], "/hawtio/jolokia"])           
            allJson.append(data)
json_data= json.dumps(allJson)

print(json.dumps(json_data))
with open('./OpenHAWT.temp', 'r') as original:
    data = original.read()
    data = data.replace("TEMP_PLACHOLDER",json.dumps(json_data))
    with open('./OpenHAWTIO.html', 'w') as modified:
            modified.write(data)

# print(data["applications"]["application"][0]["name"])
