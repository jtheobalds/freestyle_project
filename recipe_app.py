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
if recipe_list == []:
    print("I'm sorry. I could not find any recipes for that item.")
    quit("Please come back if you think of anything else you would like to explore.")
else:
    print("""
    ----------------------------------------------------
                        RECIPES
    ----------------------------------------------------
    """)
    for rec in recipe_list:
        soci_rank = "{0:.2f}".format(rec["social_rank"])
        recipe_name = rec["title"]
        recipe_name = recipe_name.title()
        source_link = rec["source_url"]
        print(rec["title"] + " | " + rec["publisher"] + " | " + soci_rank)

        
        print("----------------------------------------------------------")
        next_move = input("What would you like to do next? ").title()
        print("----------------------------------------------------------")
        if next_move == "ingredients".title():
            recipe_request = input("For which recipe would you like to see the ingredients? ").title()
#TODO ERROR MESSAGE'
            f2f_url = matching_recipe(recipe_request)
            source_url = matching_url(recipe_request)
            new_response = requests.get(f2f_url)
            response_html = new_response.text
            soup = BeautifulSoup(response_html, "lxml")
            ingredient_names = soup.find_all("li", itemprop="ingredients")
            # print(ingredient_names)
            ingredients = []
            for ingredient in ingredient_names:
                rec_ingr = ingredient.text.strip()
                # if rec_ingr.title() in allergens:
                #     rec_ingr = rec_ingr + "*"
                ingredients.append(rec_ingr)
            ingredients.append(source_url)
            for allergen in allergens:
                if any(allergen in ing for ing in ingredients):
                    print("*** This recipe contains at least 1 ingredient that you are allergic to. ***")
            print(ingredients)
