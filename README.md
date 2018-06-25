# freestyle_project

# Recipe and Lists App

This is a python application that will allow a user to search for recipes based
on food items and send list of ingredients to Google Keep

## Installing the program

## Setup
install requirements.txt

### Environment Variables

First, you will need to obtain a [Food2Fork API key](https://food2fork.com/about/api). This key will be used to access data from the Food2Fork website and download recipes.

This key should be kept private. In order to keep it from being tracked in the main application, you will need to set up an environment variable named `FOOD_API` in the command line.

Windows users can set the variable in the command line using the `set` command:
```sh
# Windows Command Prompt:
set  FOOD_API=730284y5uf508930
```

while Mac users can use `~/.bash_profile`:
```sh
# Mac text editor
export FOOD_API=730284y5uf508930
```
Mac users will need to exit and re-enter for changes to take effect.

Users will also need to set environment variables for their Google username called `g_user` and their Google password called `g_pass`. These will allow the ingredients to be published to the individual's Google Keep file (only Google accounts, not NYU quite yet).
```sh
# Windows users
set g_user=pythonprincess0
set g_pass=mypassword123

# Mac users
export g_user=pythonprincess0
export g_pass=mypassword123
```

## Run the app

After all of the preparation steps have been take, the recipe app can be run:
```sh
# Homebrew-installed Python 3.x on Mac OS:
python3 recipe_app.py

# All others:
python recipe_app.py
```
