import random

A = ["liver","milk","eggs","Swiss cheese","cheddar cheese","sweet potatoes",
     "carrots","squash","spinach"]
B1 = ["pork chops","ham","soymilk","watermelons","acorn squash"]
B2 = ["milk","yogurt","cheese","grains","cereals","liver"]
B3 = ["meat","poultry","fish","grains","mushrooms","potatoes","peanut butter"]
B5 = ["chicken","whole grains","broccoli","mushrooms","avocados","tomatoes"]
B6 = ["meat", "fish", "poultry", "legumes", "tofu","soy products", "potatoes",
      "bananas", "watermelons"]
B12 = ["meat","poultry","fish","milk","cheese","eggs","cereals","soymilk"]
Biotin = ["liver","whole grains","organ meats","egg yolks","fish"]
C = ["juice","orange juice","potatoes","broccoli","bell peppers","spinach",
     "strawberries","tomatoes","Brussels sprouts"]
Choline = ["milk","eggs","liver","peanuts"]
D = ["milk","margerine","cereals","fatty fish"]
E = ["vegetable oil","salad dressing","wheat germ","leafy greens","vegetables",
     "whole grains","nuts"]
Folate = ["grains","cereals","asparagus","okra","spinach","broccoli","legumes",
      "black-eyed peas","chickpeas","orange juice","tomato juice"]
K = ["cabbage","liver","eggs","milk","broccoli","sprouts","kale","collards",
     "greens"]

Calcium = ["yogurt","milk","cheese","tofu","sardines","salmon","juice",
           "leafy greens","vegetables","broccoli","kale"]
Chloride = ["salt","soy sauce","processed foods"]
Chromium = ["meat","poultry","some cereals","nuts","cheese"]
Copper = ["liver","shellfish","nuts","seeds","whole grains","beans","prunes"]
Flouride = ["flouridated water","toothpaste","marine fish","teas"]
Iodine = ["Iodized salt","processed foods","seafood"]
Iron = ["red meat","poultry","eggs","fruits","green vegetables","bread",
        "grains"]
Magnesium = ["spinach","broccoli","legumes","cashews","sunflower seeds",
             "seeds","halibut","whole-wheat bread","milk"]
Manganese = ["nuts","legumes","whole grains","teas"]
Molybdenum = ["legumes","nuts","grains","milk"]
Phosphorus = ["milk","dairy","meat","fish","poultry","eggs","liver",
              "green peas","broccoli","potatoes","almonds"]
Potassium = ["meat","milk","fruits","vegetables","grains","legumes"]
Selenium = ["organ meats","seafood","walnuts","grains"]
Sulfur = ["meats","fish","poultry","nuts","legumes"]
Zinc = ["red meats","poultry","oysters","cereals","beans","nuts"]

all_foods = ['liver', 'milk', 'eggs', 'Swiss cheese', 'cheddar cheese', 
             'sweet potatoes', 'carrots', 'squash', 'spinach', 'pork chops', 
             'ham', 'soymilk', 'watermelons', 'acorn squash', 'yogurt', 
             'cheese', 'grains', 'cereals', 'meat', 'poultry', 'fish', 
             'mushrooms', 'potatoes', 'peanut butter', 'chicken', 
             'whole grains', 'broccoli', 'avocados', 'tomatoes', 'legumes', 
             'tofu', 'soy products', 'bananas', 'organ meats', 'egg yolks', 
             'juice', 'orange juice', 'bell peppers', 'strawberries', 
             'Brussels sprouts', 'peanuts', 'margerine', 'fatty fish', 
             'vegetable oil', 'salad dressing', 'wheat germ', 'leafy greens', 
             'vegetables', 'nuts', 'asparagus', 'okra', 'black-eyed peas', 
             'chickpeas', 'tomato juice', 'cabbage', 'sprouts', 'kale', 
             'collards', 'greens', 'sardines', 'salmon', 'salt', 'soy sauce', 
             'processed foods', 'some cereals', 'shellfish', 'seeds', 'beans', 
             'prunes', 'flouridated water', 'toothpaste', 'marine fish', 
             'teas', 'red meat', 'fruits', 'green vegetables', 'bread', 
             'cashews', 'sunflower seeds', 'halibut', 'whole-wheat bread', 
             'dairy', 'green peas', 'almonds', 'seafood', 'walnuts', 'meats', 
             'red meats', 'oysters']

vitamins_and_minerals = [A,B1,B2,B3,B5,B6,B12,Biotin,C,Choline,D,E,Folate,K,
                         Calcium,Chloride,Chromium,Copper,Flouride,Iron,
                         Manganese,Magnesium,Molybdenum,Potassium,Phosphorus,
                         Selenium,Sulfur,Zinc]

vitamins_and_minerals_names = ["A","B1","B2","B3","B5","B6","B12","Biotin","C",
                               "Choline","D","E","Folate","K","Calcium",
                               "Chloride","Chromium","Copper","Flouride",
                               "Iron","Manganese","Magnesium","Molybdenum",
                               "Potassium","Phosphorus","Selenium","Sulfur",
                               "Zinc"]

def return_foods():
	foods = []
	for i in vitamins_and_minerals:
		for e in i:
			if e not in foods:
				foods.append(e)
	print	 foods

return_foods()

"""final_meal = []

i = 0

while i < len(vitamins_and_minerals):
	food = vitamins_and_minerals[i]
	food = food[random.randint(0,len(food)-1)]
	if food not in final_meal:
		final_meal = final_meal + [vitamins_and_minerals_names[i] + ": " + food]
	i += 1

for e in final_meal:
	print e"""