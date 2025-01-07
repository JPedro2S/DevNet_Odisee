import json
import requests
requests.packages.urllib3.disable_warnings()

IP_ADDRESS = "192.168.56.101"
RESTCONF_USERNAME = "cisco"
RESTCONF_PASSWORD = "cisco123!"
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)

api_url = f"https://{IP_ADDRESS}/restconf/data/ietf-interfaces:interfaces/interface=Loopback11"
headers = { "Accept": "application/yang-data+xml",  "Content-type":"application/yang-data+json" }

resp = requests.delete(api_url, auth=basicauth, headers=headers, verify=False)

print(resp.status_code)

response = resp.text
print(response)