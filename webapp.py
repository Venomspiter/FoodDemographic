from flask import Flask, render_template, request, Markup, flash, Markup
import os 
import json
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
@app.route("/p1")
def render_fact1():
    food = request.args['options']
    return render_template('page1.html', cookFact =  food_fact1(food), option = get_food_options())

@app.route("/p2")
def render_fact2():
    food = request.args['options']
    return render_template('page2.html', cookFact =  food_fact2(food), option = get_food_options())

@app.route("/p3")
def render_fact3():
    food = request.args['options']
    return render_template('page3.html', cookFact =  food_fact3(food), option = get_food_options())
    

def get_food_options():
        with open('food.json') as food_data:
            foodList = json.load(food_data)
        options = ""
        foodType = ""
        for x in foodList:
            if  x["Category"] != foodType:
                options += Markup("<option value=\"" + x["Category"] + "\">" + x["Category"] + "</option>")
                foodType = x["Category"]
        return render_template('index.html', option = options)

@app.route("/")
def render_main():
    return get_food_options()

def food_fact1(food):
    with open('food.json') as food_data:
            foodlist = json.load(food_data)
    total = 0
    for c in foodlist:
        if food == c['Category']:
            total = total + c['Major Minerals']['Sodium']
    return total

def food_fact2(food):
    with open('food.json') as food_data:
            foodlist = json.load(food_data)
    fat = 0
    for c in foodlist:
        if food == c['Category']:
            total = c['Fat']['Saturated Fat']
    return total

def food_fact3(food):
    with open('food.json') as food_data:
            foodlist = json.load(food_data)
    Cholesterol = 0
    for c in foodlist:
        if food == c['Category']:
            Cholesterol = c['Cholesterol']
    return Cholesterol
if __name__== '__main__':
    main()
    app.run(debug=False, port=54321)
