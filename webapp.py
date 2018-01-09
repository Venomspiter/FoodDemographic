from flask import Flask, render_template, request, Markup, flash, Markup
import os 
import json
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
@app.route("/")
def render_main():
    return get_food_options()
@app.route("/p1")
def run_page1():
    return render_template('page1.html', options = get_food_list())
@app.route("/p2")
def run_page2():
    return render_template('page2.html', options = get_food_list())
@app.route("/p3")
def run_page3():
    return render_template('page3.html', options = get_food_list())
@app.route("/page1")
def render_fact1():   
	food1 =  request.args['food']
	return render_template('page1.html', cookFact =  food_fact1(food1), options = get_food_list())
@app.route("/page2")
def render_fact2():
	food2 =  request.args['food']
	return render_template('page2.html', cookFact =  food_fact2(food2), options = get_food_list())
@app.route("/page3")
def render_fact3():
    food3 =  request.args['food']
    return render_template('page3.html', cookFact =  food_fact3(food3), options = get_food_list())
def get_food_options():
        with open('food.json') as food_data:
            foodList = json.load(food_data)
        option = ""
        foodType = ""
        for x in foodList:
            if  x["Description"] != foodType:
                option += Markup("<option value=\"" + x["Description"] + "\">" + x["Description"] + "</option>")
                foodType = x["Description"]
        return render_template('index.html', options = option)
def get_food_list():
        with open('food.json') as food_data:
            foodList = json.load(food_data)
        option = ""
        foodType = ""
        for x in foodList:
            if  x["Description"] != foodType:
                if x["Description"] not in option:
                    option += Markup("<option value=\"" + x["Description"] + "\">" + x["Description"] + "</option>")
                    foodType = x["Description"]
        return option
def food_fact1(food):
    with open('food.json') as food_data:
        foodlist = json.load(food_data)
        total = 0
        for c in foodlist:
            if food == c['Description']:
                total = total + c['Data']['Major Minerals']['Sodium']
        if total <= 250:
            return food + " has a little salt in it. Nearly " + str(total) + " salt"
        if total >= 250 and total <= 750:
            return food + " has about medium salt. Around: " + str(total) + " units of salt in it."
        else:
            return food + " has a heck of a lot of salt in it. about " + str(total) +" units."

def food_fact2(food):
    with open('food.json') as food_data:
        foodlist = json.load(food_data)
    fat = 0
    for c in foodlist:
        if food == c['Description']:
            fat = c['Data']['Fat']['Saturated Fat']
    return food + " has " + str(fat) + " fat in it"

def food_fact3(food):
    with open('food.json') as food_data:
        foodlist = json.load(food_data)
    Cholesterol = 0
    for c in foodlist:
        if food == c['Description']:
            Cholesterol = c['Data']['Cholesterol']
    return food + " has " + str(Cholesterol) + " cholestorol."
if __name__== '__main__':
    app.run(debug=True, port=54321)
