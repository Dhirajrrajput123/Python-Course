# write a function in Python, you can use the *def* keyword followed by the function name, 

# def  name():
#     print("how are you")
# name()

dir={}


def add(dir,name,age):
    dir[name]=age

def update(dir,name,age):
    dir[name]=age

def delete(dir,name):
    dir.pop(name)





 

# Input: Add "John": 25, Update "John": 26, Delete "John"
add(dir,"John",25)

print(dir)

update(dir,"John",26)

print(dir)

delete(dir,"John")

print(dir)


