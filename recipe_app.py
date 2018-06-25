import json
import requests
import os
from bs4 import BeautifulSoup

api_key = os.environ.get("FOOD_API")

food_item = input("Please input a meal (e.g. pasta), recipe ingredient (e.g. chicken), style (e.g. Mexican), or cooking method (e.g. grilled) : ")

request_url = f"http://food2fork.com/api/search?key={api_key}&q={food_item}"
response = requests.get(request_url)
# pdb.set_trace()
response_output = json.loads(response.text)
# print(response_output)
# pdb.set_trace()

recipe_list = response_output["recipes"]
