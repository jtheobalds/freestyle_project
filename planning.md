# Project Planning

## Problem statement

### Primary User
Me (a person who wants to try new recipes without spending a lot of time making
  lists)

### User Needs statement

As a person who enjoys new recipes but hates making lists, I need a quicker way
to find delicious recipes using the food items I crave or already have and
create a grocery list.

### As-is Process Description

  1. Requests food item input
  2. Obtain a list of possible recipes

### To-be Process Description
  1. Requests food item input
  2. Run a script to deliver possible recipes to be chosen from and check for
      existence of allergens.
  3. Upload ingredients to a Google Keep list


## Information Requirements

### Information Inputs

  1. Food item wanted in the recipe
  2. List of allergens that should be avoided
  3. Chosen option of what to do with the list of recipes

### Information Outputs
  1. Name of the recipes
  2. List of recipes
  3. Warning if chosen recipe contains allergens
  4. Based on chosen option: List of food items needed, Image of recipe, Directions of how to make, More recipes, ingredients in Keep list

## Technology Requirements

### APIs and Web Service Requirements

The user will need to obtain a [Food2Fork API key](https://food2fork.com/about/api).
The user will also need a Google or Gmail account which contains a username and password.

### Python Package Requirements
Third-party packages:
  1. `pytest` will be used for testing purposes
  2. After some research, I found the `gkeepapi` package that should allow me to
      publish to Google Keep
  3. The `beautifulsoup4` package will be needed for scraping the recipe websites

Modules:
  1. `json`
  2. `requests`
  3. `os`
  4. `BeautifulSoup`
  4. `gkeepapi`
  5. `webbrowswer

### Hardware Requirements

The application will be running on my local machine.
