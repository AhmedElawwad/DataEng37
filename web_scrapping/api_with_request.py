
import requests
from pprint import pprint
import json

# pc_req = requests.get("https://api.postcodes.io/postcodes/SE12 0NB")

# print(pc_req, type(pc_req))
#
# if pc_req.status_code == 200:
#     # pprint(dict(pc_req.headers), sort_dicts=Fase)l # pprint make it better to read
#     # print(type(pc_req.content))
#     # print(pc_req.content)
#     postcode = json.loads(pc_req.content)
#     #print(postcode) # to get it as dictionary
#     # print(postcode['admin_district'])
#     result = postcode['result']
#     print(result['admin_district'])



"""
Post request
"""
header = {'Content-Type': 'application/json'}
body = {'postcodes': ['PR3 0SG', "M45 6GN", "EX165BL"]}


url = "https://api.postcodes.io/postcodes/"
pc_req = requests.post(url, headers=header, data = json.dumps(body)) # we used json.dump to make sure that server gets json and not a dict

pcs = pc_req.json()['result']
# pprint(pcs, sort_dicts=False)

for pc_data in pcs:
    result = pc_data['result']
    print("----------",result['postcode'],"--------")
    print(result['admin_ward'])
    print(result['eastings'], result['northings'])
    print(result['codes']['nuts'])

pprint(pcs)

# admin_ward, easting, northin

