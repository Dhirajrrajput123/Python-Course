sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]


# keys = my_dict.keys()

# keys = list(my_dict)

# my_dict.pop("age") for deletw the key from the dirictory


newdir={}

for key in keys:
         newdir[key]=sample_dict[key]


print(newdir)


