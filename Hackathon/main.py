from tkinter import *
import requests
from pprint import pprint

root = Tk()


def preferencesget():
    print(diet1.get(), diet2.get(), diet3.get(), diet4.get(), diet5.get(), diet6.get(), diet7.get(), diet8.get(),
          diet9.get(), diet10.get())
    print(intolerances1.get(), intolerances2.get(), intolerances3.get(), intolerances4.get(), intolerances5.get(),
          intolerances6.get(), intolerances7.get(), intolerances8.get(), intolerances9.get(), intolerances10.get(),
          intolerances11.get(), intolerances12.get())
    print(cuisinevalue.get())
    print(mealtypes1.get(), mealtypes2.get(), mealtypes3.get(), mealtypes4.get(), mealtypes5.get(), mealtypes6.get(),
          mealtypes7.get(), mealtypes8.get(), mealtypes9.get(), mealtypes10.get(), mealtypes11.get(), mealtypes12.get(),
          mealtypes13.get(), mealtypes14.get())
    print(ingredientsvalue.get())

    with open("favorites.txt", "a") as f:
        f.write(
            f"{diet1.get(), diet2.get(), diet3.get(), diet4.get(), diet5.get(), diet6.get(), diet7.get(), diet8.get(),}\n ")
        f.write(
            f"{intolerances1.get(), intolerances2.get(), intolerances3.get(), intolerances4.get(), intolerances5.get(), intolerances6.get(), intolerances7.get(), intolerances8.get(), intolerances9.get(), intolerances10.get(), intolerances11.get(), intolerances12.get()}\n ")
        f.write(f"{cuisinevalue.get()}\n ")
        f.write(
            f"{mealtypes1.get(), mealtypes2.get(), mealtypes3.get(), mealtypes4.get(), mealtypes5.get(), mealtypes6.get(), mealtypes7.get(), mealtypes8.get(), mealtypes9.get(), mealtypes10.get(), mealtypes11.get(), mealtypes12.get(), mealtypes13.get(), mealtypes14.get()}\n ")
        f.write(f"{ingredientsvalue.get()}\n ")



def getrecipe():
    params = {
        'apiKey': '57d54cb4b9bc42178161912eb40b75e7',
        'query': (
        mealtypes1.get(), mealtypes2.get(), mealtypes3.get(), mealtypes4.get(), mealtypes5.get(), mealtypes6.get(),
        mealtypes7.get(), mealtypes8.get(), mealtypes9.get(), mealtypes10.get(), mealtypes11.get(), mealtypes12.get(),
        mealtypes13.get(), mealtypes14.get()),
        'cuisine': cuisinevalue.get(),
        'diet': (diet1.get(), diet2.get(), diet3.get(), diet4.get(), diet5.get(), diet6.get(), diet7.get(), diet8.get(),
                 diet9.get(), diet10.get()),
        'number': 10,
        'includeInstructions': True
    }
    response = requests.get('https://api.spoonacular.com/recipes/complexSearch?apiKey=57d54cb4b9bc42178161912eb40b75e7',
                            params=params)
    data = response.json()
    pprint(data, indent=4)


# with open("favorites.txt", "a") as f:
# f.write(f"{diet1.get(), diet2.get(), diet3.get(), diet4.get(), diet5.get(), diet6.get(), diet7.get(), diet8.get(), }\n ")
# f.write(f"{intolerances1.get(), intolerances2.get(), intolerances3.get(), intolerances4.get(), intolerances5.get(), intolerances6.get(), intolerances7.get(), intolerances8.get(),intolerances9.get(), intolerances10.get(), intolerances11.get(), intolerances12.get()}\n ")
# f.write(f"{cuisinevalue.get()}\n ")
# f.write(f"{mealtypes1.get(), mealtypes2.get(), mealtypes3.get(), mealtypes4.get(), mealtypes5.get(), mealtypes6.get(),mealtypes7.get(), mealtypes8.get(), mealtypes9.get(), mealtypes10.get(), mealtypes11.get(), mealtypes12.get(), mealtypes13.get(), mealtypes14.get()}\n ")
# f.write(f"{ingredientsvalue.get()}\n ")
# f.write(f"{response.json()}\n ")

Label(root, text="The Munchies Generator", font="comicsansms 25 bold").grid(row=0, column=1)

Label(root, text="--------------------------------------------------------").grid(row=1, column=1)

Label(root, text="Diet Preferences", font="comicsansms 20 bold").grid(row=2, column=1)

diet1 = StringVar()
Checkbutton(root, text="Gluten-Free", variable=diet1, onvalue="Gluten-Free").grid(row=3, sticky=W)
diet2 = StringVar()
Checkbutton(root, text="Ketogenic    ", variable=diet2, onvalue="Ketogenic").grid(row=3, column=1, )
diet3 = StringVar()
Checkbutton(root, text="Vegeterian", variable=diet3, onvalue="Vegeterian").grid(row=3, column=2, sticky=W)
diet4 = StringVar()
Checkbutton(root, text="Lacto-Vegeterian", variable=diet4, onvalue="Lacto-Vegeterian").grid(row=4, sticky=W)
diet5 = StringVar()
Checkbutton(root, text="Ovo-Vegeterian", variable=diet5, onvalue="Ovo-Vegeterian").grid(row=4, column=1, )
diet6 = StringVar()
Checkbutton(root, text="Vegan", variable=diet6, onvalue="Vegan").grid(row=4, column=2, sticky=W)
diet7 = StringVar()
Checkbutton(root, text="Pesceterian", variable=diet7, onvalue="Pesceterian").grid(row=5, sticky=W)
diet8 = StringVar()
Checkbutton(root, text="Paleo        ", variable=diet8, onvalue="Paleo").grid(row=5, column=1, )
diet9 = StringVar()
Checkbutton(root, text="Primal", variable=diet9, onvalue="Primal").grid(row=5, column=2, sticky=W)
diet10 = StringVar()
Checkbutton(root, text="Whole30", variable=diet10, onvalue="Whole30").grid(row=6, sticky=W)

Label(root, text="--------------------------------------------------------").grid(row=7, column=1)

Label(root, text="Intolerances", font="comicsansms 20 bold").grid(row=8, column=1)

intolerances1 = StringVar()
Checkbutton(root, text="Diary", variable=intolerances1, onvalue="Diary").grid(row=9, sticky=W)
intolerances2 = StringVar()
Checkbutton(root, text="Peanut", variable=intolerances2, onvalue="Peanut").grid(row=9, column=1, )
intolerances3 = StringVar()
Checkbutton(root, text="Soy", variable=intolerances3, onvalue="Soy").grid(row=9, column=2, sticky=W)
intolerances4 = StringVar()
Checkbutton(root, text="Egg", variable=intolerances4, onvalue="Egg").grid(row=10, sticky=W)
intolerances5 = StringVar()
Checkbutton(root, text="Seafood", variable=intolerances5, onvalue="Seafood").grid(row=10, column=1, )
intolerances6 = StringVar()
Checkbutton(root, text="Sulfite", variable=intolerances6, onvalue="Sulfite").grid(row=10, column=2, sticky=W)
intolerances7 = StringVar()
Checkbutton(root, text="Gluten", variable=intolerances7, onvalue="Gluten").grid(row=11, sticky=W)
intolerances8 = StringVar()
Checkbutton(root, text="Sesame", variable=intolerances8, onvalue="Sesame").grid(row=11, column=1, )
intolerances9 = StringVar()
Checkbutton(root, text="Tree Nut", variable=intolerances9, onvalue="Tree Nut").grid(row=11, column=2, sticky=W)
intolerances10 = StringVar()
Checkbutton(root, text="Grain", variable=intolerances10, onvalue="Grain").grid(row=12, sticky=W)
intolerances11 = StringVar()
Checkbutton(root, text="Shellfish", variable=intolerances11, onvalue="Shellfish").grid(row=12, column=1, )
intolerances12 = StringVar()
Checkbutton(root, text="Wheat", variable=intolerances12, onvalue="Wheat").grid(row=12, column=2, sticky=W)

Label(root, text="--------------------------------------------------------").grid(row=13, column=1)

cuisine = Label(root, text="Cuisine", font="comicsansms 20 bold").grid(row=14, column=1)
cuisinevalue = StringVar()
cuisineentry = Entry(root, textvariable=cuisinevalue).grid(row=15, column=1)

Label(root, text="--------------------------------------------------------").grid(row=16, column=1)


Label(root, text="Meal", font="comicsansms 20 bold").grid(row=17, column=1)

mealtypes1 = StringVar()
Checkbutton(root, text="Main Course", variable=mealtypes1, onvalue="Main Course").grid(row=18, sticky=W)
mealtypes2 = StringVar()
Checkbutton(root, text="Bread    ", variable=mealtypes2, onvalue="Bread").grid(row=18, column=1, )
mealtypes3 = StringVar()
Checkbutton(root, text="Marinade", variable=mealtypes3, onvalue="Marinade").grid(row=18, column=2, sticky=W)
mealtypes4 = StringVar()
Checkbutton(root, text="Side Dish", variable=mealtypes4, onvalue="Side Dish").grid(row=19, sticky=W)
mealtypes5 = StringVar()
Checkbutton(root, text="Breakfast", variable=mealtypes5, onvalue="Breakfast").grid(row=19, column=1, )
mealtypes6 = StringVar()
Checkbutton(root, text="Fingerfood", variable=mealtypes6, onvalue="Fingerfood").grid(row=19, column=2, sticky=W)
mealtypes7 = StringVar()
Checkbutton(root, text="Dessert", variable=mealtypes7, onvalue="Dessert").grid(row=20, sticky=W)
mealtypes8 = StringVar()
Checkbutton(root, text="Soup     ", variable=mealtypes8, onvalue="Soup").grid(row=20, column=1, )
mealtypes9 = StringVar()
Checkbutton(root, text="Snack", variable=mealtypes9, onvalue="Snack").grid(row=20, column=2, sticky=W)
mealtypes10 = StringVar()
Checkbutton(root, text="Appetizer", variable=mealtypes10, onvalue="Appetizer").grid(row=21, column=1, )
mealtypes11 = StringVar()
Checkbutton(root, text="Beverage", variable=mealtypes11, onvalue="Beverage").grid(row=21, column=2, sticky=W)
mealtypes12 = StringVar()
Checkbutton(root, text="Drink", variable=mealtypes12, onvalue="Drink").grid(row=21, sticky=W)
mealtypes13 = StringVar()
Checkbutton(root, text="Salad    ", variable=mealtypes13, onvalue="Salad").grid(row=22, column=1, )
mealtypes14 = StringVar()
Checkbutton(root, text="Sauce", variable=mealtypes14, onvalue="Sauce").grid(row=22, column=2, sticky=W)

Label(root, text="--------------------------------------------------------").grid(row=23, column=1)

ingredients = Label(root, text="Include Ingredients", font="comicsansms 20 bold").grid(row=24, column=1)
ingredients = Label(root, text="Type igredients separated by a ','. Example: garlic,pepper,tomato",
                    font="comicsansms 10 ").grid(row=26, column=1)
Label(root, text="We're assuming that you have the basics: Salt,Sugar,Flour,Oil", font="comicsansms 10").grid(row=27,
                                                                                                              column=1)
ingredientsvalue = StringVar()
ingredientsentry = Entry(root, textvariable=ingredientsvalue).grid(row=28, column=1)

Label(root, text="--------------------------------------------------------").grid(row=29, column=1)

Button(root, text="Save Preferences", font="comicsansms 23 bold", command=preferencesget).grid(row=30, column=1)
Button(root, text="Get Recipe", font="comicsansms 23 bold", command=getrecipe).grid(row=31, column=1)


root.mainloop()