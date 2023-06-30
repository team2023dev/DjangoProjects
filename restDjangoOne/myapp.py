import requests
import json
URL='http://127.0.0.1:8000/stucreate/'

body={
    'name':'Kamal',
    'roll':104,
    'city':'Lagos'
}
json_data=json.dumps(body)
response=requests.post(url=URL,data=json_data)
data=response.json()
print(data)