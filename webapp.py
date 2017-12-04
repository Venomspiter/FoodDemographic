from flask import Flask, render_template, request, Markup, flash, Markup
import os 
import json
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
@app.route("/app")
def render_fact():
    state = request.args['options']
    return render_template('page1.html', cookFact =  food_fact(food), option = get_food_options())
    

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
    return get_state_options()

def food_fact(food):
    with open('food.json') as food_data:
            foodlist = json.load(food_data)
    total = 0
    for c in foodlist:
        if food == c['Category']:
            total = total + c['Major Minerals']['sodium']
    return total
if __name__== '__main__':
    main()
    app.run(debug=False, port=54321)
