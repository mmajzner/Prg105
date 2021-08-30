"""
Find a recipe online, provide a link to the recipe in the comments.
Display the ingredients with amounts and list the servings that will
be made with the recipe. Ask the user to enter how many servings they
would like to make, and display the required amount of ingredients they
will need. Format to one decimal place.

https://www.tasteofhome.com/recipes/ultimate-double-chocolate-brownies/
"""


baking_cocoa_cups = .75/36
baking_soda_tsp = .5/36
butter_cups = 2/3/36
boiling_water_cups = .5/36
sugar_cups = 2/36
large_eggs = 2/36
flour_cups = 1.3333333/36
vanilla_extract_tsp = 1/36
salt_tsp = .25/36
chopped_pecans_cups = .5/36
chocolate_chunks_cups = 2/36

serving = int(input("How many servings would you like to make? - "))

baking_cocoa_cups = baking_cocoa_cups * serving
baking_soda_tsp = baking_soda_tsp * serving
butter_cups = butter_cups * serving
boiling_water_cups = boiling_water_cups * serving
sugar_cups = sugar_cups * serving
large_eggs = large_eggs * serving
flour_cups = flour_cups * serving
vanilla_extract_tsp = vanilla_extract_tsp * serving
salt_tsp = salt_tsp * serving
chopped_pecans_cups = chopped_pecans_cups * serving
chocolate_chunks_cups = chocolate_chunks_cups * serving

print("You will need: " + str(format(baking_cocoa_cups, ",.2f")) + " cup(s) of baking cocoa")
print("You will need: " + str(format(baking_soda_tsp, ",.2f")) + " teaspoon(s) of baking soda")
print("You will need: " + str(format(butter_cups, ",.2f")) + " cup(s) of butter, melted, divided")
print("You will need: " + str(format(boiling_water_cups, ",.2f")) + " cup(s) of boiling water")
print("You will need: " + str(format(sugar_cups, ",.2f")) + " cup(s) of sugar")
print("You will need: " + str(format(large_eggs, ",.2f")) + " large egg(s), room temperature")
print("You will need: " + str(format(flour_cups, ",.2f")) + " cup(s) of all-purpose flour")
print("You will need: " + str(format(vanilla_extract_tsp, ",.2f")) + " teaspoon(s) of vanilla extract")
print("You will need: " + str(format(salt_tsp, ",.2f")) + " teaspoon(s) of salt")
print("You will need: " + str(format(chopped_pecans_cups, ",.2f")) + " cup(s) of coarsely chopped pecans")
print("You will need: " + str(format(chocolate_chunks_cups, ",.2f")) + " cup(s) of semisweet chocolate chunks")
