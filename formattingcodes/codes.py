import requests
import json
import re
import sys

api_url = 'http://api.postcodes.io/postcodes/'

def get_detail_code(code):
  if validate_code(code) and code != None:
    try:
      response = requests.get(api_url + code)
      response = json.loads(response.text)
      if response.get('status') == 200:
        print response.get('result')
      else:
        print 'Not found!'
    except requests.exceptions.RequestException as e:
      print e
      sys.exit(1)
  else:
    print 'Postcode is invalid!'

def validate_code(code):
  try:
    response_valid = requests.get(api_url + code + '/validate')
    response_valid = json.loads(response_valid.text)
    return response_valid.get('result')
  except requests.exceptions.RequestException as e:
    print e
    sys.exit(1)
