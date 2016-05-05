import pandas

food_info = pandas.read_csv("ABBREV.csv")

#print(food_info)

first_five_rows = food_info.head()

print(first_five_rows)