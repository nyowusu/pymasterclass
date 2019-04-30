fruit = {"orange":"a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage":"every child's favourite",
       "sprouts":"hmmmmm, lovely",
       "spinach":"may i have some fruit please"}

print(veg)

veggie = veg.copy()

print("="*50)

print(veggie)

veggie.update(fruit)

print("="*50)

print(veggie)