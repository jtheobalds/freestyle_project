import json
import requests
import os
import pdb
from bs4 import BeautifulSoup
import gkeepapi
import webbrowser

api_key = os.environ.get("FOOD_API")
goog_username = os.environ.get("g_user")
goog_password = os.environ.get("g_pass")


def matching_recipe(recipe_request):
    recipe_url = [r for r in recipe_list if r["title"] == recipe_request]
    return recipe_url[0]["f2f_url"]

def matching_url(recipe_request):
    official_url = [r for r in recipe_list if r["title"] == recipe_request]
    return official_url[0]["source_url"]

def matching_source(recipe_request):
    off_source_url = [r for r in recipe_list if r["title"] == recipe_request]
    webbrowser.open(off_source_url[0]["source_url"])

def matching_pic(recipe_request):
    picture_url = [r for r in recipe_list if r["title"] == pic_request]
    webbrowser.open(picture_url[0]["image_url"])

def menu(recipe_count=30):
    menu = f"""
    ------------------------------------------------------------------
                RECIPE OPTIONS
    -------------------------------------------------------------------
        operation     | description
        ------------  | -------------
        'More'        | Prints 30 more recipe options.
        'Ingredients' | Displays a list of ingredients for the recipe.
        'Directions'  | Opens the source directions in web browser
        'Image'       | Opens a picture of the recipe in web browser.
        'Send'        | Sends a list of ingredients and link to the source
                        to a Google Keep list.
        'Done'        | Exits the program.
    """
    return menu

food_item = input("Please input a meal (e.g. pasta), recipe ingredient (e.g. chicken), style (e.g. Mexican), or cooking method (e.g. grilled) : ")

allergens = []
food_allergies = input("Do you have any food allergies (yes or no)? ").title()
if food_allergies == "yes".title():
    while True:
        try:
            allergen = input("What are you allergic to (please input one at a time)? ").title()
            allergen = allergen.title()
            if allergen == "done".title():
                allergen_count = len(allergens)
                allergen_count = str(allergen_count)
                print(allergen_count + " food allergens listed")
                break
            else:
                allergens.append(allergen)
        except:
            print("error")
elif food_allergies == "no".title():
    allergen_count = len(allergens)
    allergen_count = str(allergen_count)
    print(allergen_count + " food allergies listed")
else:
    print("I'm sorry. Please input 'yes' or 'no'.")

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
            f2f_url = matching_recipe(recipe_request)
            source_url = matching_url(recipe_request)
            new_response = requests.get(f2f_url)
            response_html = new_response.text
            soup = BeautifulSoup(response_html, "lxml")
            ingredient_names = soup.find_all("li", itemprop="ingredients")
            ingredients = []
            for ingredient in ingredient_names:
                rec_ingr = ingredient.text.strip()
                ingredients.append(rec_ingr)
            ingredients.append(source_url)
            for allergen in allergens:
                if any(allergen in ing for ing in ingredients):
                    print("*** This recipe contains an ingredient that you are allergic to. ***")
            print(ingredients)
        elif next_move == "image".title():
            pic_request = input("Which recipe would you like to see? ").title()
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
            recipe_list = response_output["recipes"]
            for rec in recipe_list:
                soci_rank = "{0:.2f}".format(rec["social_rank"])
                print(rec["title"] + " | " + rec["publisher"] + " | " + soci_rank)
        elif next_move == "send".title():
            recipe_request = input("Which recipe do you want in your list? ").title()
            f2f_url = matching_recipe(recipe_request)
            source_url = matching_url(recipe_request)
            new_response = requests.get(f2f_url)
            response_html = new_response.text
            soup = BeautifulSoup(response_html, "lxml")
            ingredient_names = soup.find_all("li", itemprop="ingredients")
            ingredients = []
            for ingredient in ingredient_names:
                rec_ingr = ingredient.text.strip()
                ingredients.append(rec_ingr)
            ingredients.append(source_url)
            keep = gkeepapi.Keep()
            keep.login(goog_username, goog_password)
            ingredient_list_param = [(f, False) for f in ingredients]
            glist = keep.createList(recipe_request, ingredient_list_param)
            glist.pinned = True
            keep.sync()
            print("""
            ----------------------------------------------------
                Sending the ingredients to your account
            ----------------------------------------------------
            """)
        elif next_move == "done".title():
            print("""
            ----------------------------------------------------
                Thank you for exploring recipes with us!
                        Now let's GET COOKING!
            ----------------------------------------------------
            """)
            break
        else:
            print("Oops! That's an invalid function. Please select an option from the menu.")
    except:
        print("""
        I'm sorry. I can't find that recipe. Please choose one from the RECIPES list above.
        """)
