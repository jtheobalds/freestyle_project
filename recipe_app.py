import json
import requests
import os
import pdb
from bs4 import BeautifulSoup
import webbrowser

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

pagination = 1

while True:
    try:
        print(menu())        
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
         elif next_move == "image".title():
            pic_request = input("Which recipe would you like to see? ").title()
#TODO ERROR MESSAGE
            print("""
            ----------------------------------------------------
                        Pulling up the image now.
            ----------------------------------------------------
            """)
            pic_url = matching_pic(pic_request)
        elif next_move == "directions".title():
            dir_request = input("For which recipe would you like to see the directions? ").title()
            print("""
            -----------------------------------------------------
                    Pulling up the directions now.
            -----------------------------------------------------
            """)
            dir_url = matching_source(dir_request)
        elif next_move == "more".title():
            pagination = pagination + 1
            request_url = f"http://food2fork.com/api/search?key=9053cc2ecc0ad5b108929907c200a9cc&q={food_item}&page={pagination}"
            response = requests.get(request_url)
            response_output = json.loads(response.text)
            # print(response_output)
            recipe_list = response_output["recipes"]
            # print(request_url)
            for rec in recipe_list:
                soci_rank = "{0:.2f}".format(rec["social_rank"])
                print(rec["title"] + " | " + rec["publisher"] + " | " + soci_rank)
        elif next_move == "send".title():
            recipe_request = input("Which recipe do you want in your list? ").title()
