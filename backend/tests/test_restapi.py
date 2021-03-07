from os import getenv
from json import loads
from random import randint
from datetime import datetime

from pymongo import MongoClient
from bson.objectid import ObjectId

from backend.services.database import DatabaseWrapper


collection = MongoClient(getenv('MONGO_URI'))['higgs']['igorm']

def setup():
    try:
        collection.delete_many({})
    except Exception as e:
        print("There was an error Setting Up:", e)

    transactions = [
        {
            'type': 'outcome',
        },
        {
            'type': 'income',
        },
        {
            'type': 'outcome',
        },
    ]

    r = collection.insert_many(transactions)    

def teardown():
    try:
        collection = MongoClient(getenv('MONGO_URI'))['higgs']['igorm']
        collection.delete_many({})
    except Exception as e:
        print("There was an error Tearing Down:", e)

def test_api_get_all(client):
    r = client.get('/api/transaction')

    assert r.status_code == 200
    assert 'transaction' in r.json.keys()
    
    for each in r.json['transaction']:
        assert each['type'] == 'outcome' or each['type'] == 'income'

def test_api_post_one(client):
    transaction = {
        'type': 'income',
    }

    r = client.post(
        '/api/transaction', 
        json=transaction, 
        headers={ "Content-Type":"application/json" })

    assert r.status_code == 200
    assert r.json['msg'] == 'done'
    assert '_id' in r.json.keys()

    result = collection.find({ '_id': ObjectId(r.json['_id']) })
    result = list(result)

    assert len(result) == 1
    assert result[0] == { '_id': ObjectId(r.json['_id']), **transaction }

def test_api_get_one(client):
    ids = list(collection.find({}))
    _id = str(ids[randint(0, len(ids) - 1)]['_id'])

    r = client.get(f'/api/transaction/{_id}')

    assert r.status_code == 200
    assert 'transaction' in r.json.keys()

    result = r.json['transaction']

    assert len(result) == 1
    assert result[0]['_id'] == _id

def test_api_put_one(client):
    ids = list(collection.find({}))
    _id = str(ids[randint(0, len(ids) - 1)]['_id'])
    
    r = client.put(
        f'/api/transaction/{_id}', 
        json={ 'type': 'income!' }, 
        headers={ 'Content-type':'application/json' })

    assert r.status_code == 200
    assert 'msg' in r.json.keys()  

    result = list(collection.find({'_id': ObjectId(_id)}))

    assert result[0]['type'] == 'income!'

def test_api_delete(client):
    ids = list(collection.find({}))
    _id = str(ids[randint(0, len(ids) - 1)]['_id'])

    r = client.delete(f'/api/transaction/{_id}')

    assert r.status_code == 200
    assert r.json['msg'] == 'done'

    result = list(collection.find({'_id': ObjectId(_id)}))

    assert result == []