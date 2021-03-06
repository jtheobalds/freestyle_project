# freestyle_project

# Recipe and Lists App

This is a python application that will allow a user to search for recipes based
on food items and view the recipe, its ingredients, and send a list of ingredients to Google Keep.

## Installing the program

In order to use the program, it must be installed. One must "fork" this repository and download the forked version using the GitHub.com online interface or the Git command-line interface. From the command-line, the repository can be downloaded by "cloning" it using:
```sh
git clone https://github.com/YOUR_USERNAME/freestyle_project.git
```

After downloading your forked repository, navigate to the root directory:

```sh
cd freestyle_project
```

Next, you will need to install the packages needed for the application. Depending on your system requirements, use one of the following commands for installation:

```sh
# Pipenv on Mac or Windows:
pipenv install -r requirements.txt

# Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

If you are using Pipenv, enter a new virtual environment (`pipenv shell`) before running any of the commands below.

All commands below assume you are running them from this repository's root directory.

## Setup

### Environment Variables

First, you will need to obtain a [Food2Fork API key](https://food2fork.com/about/api). This key will be used to access data from the Food2Fork website and download recipes.

This key should be kept private. In order to keep it from being tracked in the main application, you will need to set up an environment variable named `food_api` in the command line.

Windows users can set the variable in the command line using the `set` command:
```sh
# Windows Command Prompt example:
set  food_api=730284y5uf508930
```

while Mac users can use `~/.bash_profile`:
```sh
# Mac text editor example
export FOOD_API=730284y5uf508930
```
Mac users will need to exit and re-enter for changes to take effect.

Users will also need to set environment variables for their Google username called `g_user` and their Google password called `g_pass`. These will allow the ingredients to be published to the individual's Google Keep file (only Google accounts, not NYU quite yet).
```sh
# Windows users example
set g_user=pythonprincess0
set g_pass=mypassword123

# Mac users example
export g_user=pythonprincess0
export g_pass=mypassword123
```
If your account requires Twofactor login, you will need to create a password through Google to access the Keep file from the program.

## Using the app

After all of the preparation steps have been taken, the recipe app can be run:
```sh
# Homebrew-installed Python 3.x on Mac OS:
python3 recipe_app.py

# All others:
python recipe_app.py
```
The app will begin by asking the user to name the kind of recipe they are interested in. This can be anything from an individual ingredient, to a style of cooking, to a method of cooking.

Next, the user will input any food allergies that should be considered. 

The app will then output 30 recipes, with which the user has the option to view 'more', view the 'ingredients', view the 'directions' of how to make the recipe, view an 'image' of the recipe, or send a list of the ingredients + the original link to Google Keep. 'Directions' and 'image' will open a web browser window. The program will continue to run until the user says that they are 'Done'.
