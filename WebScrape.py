# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = "https://www.thecrimson.com/flyby/"

# query the website and return the html to the variable page
page = urllib2.urlopen("https://www.thecrimson.com/flyby/")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")

# get the menu value
menu_box = soup.find("section", attrs={"class": "widget widget-primary"})
menu = menu_box.text.strip() # strip() to remove starting and trailing

# creates a .txt file for the menu
def out():
    return menu
output = out().encode("utf-8")
file = open("Menu.txt","w")
file.write(output)
file.close()

#stores menu elements in an list foods
foods = list()
with open("Menu.txt", "r") as f:
    for line in f:
        foods.append(line)

#class Food:
#   def __init__(item=[]):
#       for x in item:
#           if "Chicken" in x or "Pork" in x or "Beef" in x:
#               food.type = "meat"
#           else:
#               food.type = "other"

#defines type function for food
def type(x,y):
    if y in x:
        return y
    return ""

#adds funny stuff to menu items
i = 0
while i < len(foods):
    if type(foods[i], "Sandwich"):
        foods[i] = foods[i].replace("Sandwich", "Mystery Combo")
    if type(foods[i], "Beef"):
        foods[i] = foods[i].replace("Beef", "Dead Dog")
    if type(foods[i], "Chicken"):
        foods[i] = "Chunks of Cold " + foods[i]
    if type(foods[i], "Pork"):
        foods[i] = foods[i].replace("Pork", "Pig Asshole")
    if type(foods[i], "Pasta") or type(foods[i], "Penne"):
        foods[i] = "Uncooked " + foods[i]
    if type(foods[i], "Dinner"):
        foods[i] = "~~Night Slop~~"
        foods.insert(i + 1, " ")
    if type(foods[i], "Lunch"):
        foods[i] = "~~Noon Slop~~"
        foods.insert(i + 1, " ")
    if type(foods[i], "Tofu"):
        foods[i] = foods[i].replace("Tofu", "Vegan Protein Brick")

    
    i += 1

#formatting


#prints foods in terminal
for x in foods:
    print(x)

# creates a .txt file for foods
with open("Foods.txt", "w") as f:
    for item in foods:
        f.write("%s\n" % item)
file.close()
