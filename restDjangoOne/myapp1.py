import requests
import json

URL='http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    res=requests.get(url=URL,headers=headers,data=json_data)
    data=res.json()
    print(data)
# get_data()

def post_data():
    data={
        'name':'Raju',
        'roll':209,
        'city':'Dhaka'
    }
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    res=requests.post(url=URL,headers=headers,data=json_data)
    data=res.json()
    print(data)

# post_data()

def update_data():
    data={
        'id':1,
        'name':'Tony',
        'roll':119
    }
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    res=requests.put(url=URL,headers=headers,data=json_data)
    data=res.json()
    print(data)

update_data()

def delete_data():
    data={
        'id':1
    }
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    res=requests.delete(url=URL,headers=headers,data=json_data)
    data=res.json()
    print(data)

# delete_data()