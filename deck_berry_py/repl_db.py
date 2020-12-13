import requests
import os
import json

db_url = os.getenv('REPLIT_DB_URL')

def set(key, val, type='string'):
  try:
    if (type == 'string'):
      return requests.post(db_url, data = { key: val })
    if (type == 'json'):
      return requests.post(db_url, data = { key: json.dumps(val)})
  except:
    return({'error': { 'message': 'There was an issue with writing to the database'}})

def get(key):
  resp = None
  try:
    resp = requests.get("{0}/{1}".format(db_url, key))
    # Return JSON dict by default
    return json.loads(resp.text)
  except:
    try:
      # Return as string if not JSON
      return resp.text
    except:
      return({'error': { 'message': 'There was an issue with getting data from the database'}})

def delete(key):
  try:
    return requests.delete("{0}/{1}".format(db_url, key))
  except:
      return({'error': { 'message': 'There was an issue with deleting data from the database'}})


def list(key):
  "List db entries that start with [key]"
  try:
    resp = requests.get('{0}?prefix={1}'.format(db_url, key))
    resp_list = resp.text.split('\n')
    return resp_list
  except:
    return({'error': { 'message': 'There was an issue with listing data from the database'}})