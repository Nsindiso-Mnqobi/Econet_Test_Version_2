import unittest
from database import Users, db
import requests
import json


url = "http://127.0.0.1:5000/location"

payload="{\n    \"Area\": \"Harare CBD\"\n}\n"
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46YnVsYXdheW8='
}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(response)

#class test_endpoint(unittest.TestCase):
    #A shop must belong to an existing area

#if __name__=="main":
    #unittest.main()
    #print(response.)

