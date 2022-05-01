import unittest
import requests
import re


url = "http://127.0.0.1:5000/location"

payload = '{\n    "Area": "Harare CBD"\n}\n'
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Basic YWRtaW46YnVsYXdheW8=",
}

response = requests.request("GET", url, headers=headers, data=payload).json()

regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
shops = response["Shops"]
shops_list = []
for shop in shops:
    shops_list.append(shops)


class test_endpoint(unittest.TestCase):
    # shops must be saved all in uppercase
    def test_capital(self):
        for shop in shops_list:
            shop_test = ""
            shop = shop_test
            self.assertTrue(shop_test.isupper())

    # No special characters should be allowed on a shop name
    def test_special(self):
        for shop in shops_list:
            shop_test = ""
            shop = shop_test
            self.assertIs(regex.search(shop), None)


if __name__ == "__main__":
    unittest.main()
