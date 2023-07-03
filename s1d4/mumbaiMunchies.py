list=[]
snacks={
    "id":1,
    "name":"samosa",
    "price":12,
    "availability":"yes"
}
list.append(snacks)
def uniquecheck(id):
    for i in list:
        if i["id"]==id:
            return False
    return True   


def addSnacks():
    id=int(input("Enter the Snacks unique id:- "))
    
    res=uniquecheck(id)
    
    while res==False:
        id=int(input("Enter the Snacks unique id:- "))    
        res=uniquecheck(id)

    name=input("Enter the Snack Name:- ")  
    price=int(input("Enter the Snack Price:- "))
    availability=input("Snacks Availavility:- ")
    newSnack={
        "id":id,
        "name":name,
        "price":price,
        "availability":availability
    }

    list.append(newSnack)
    # price( "new Snack added Successfully:-  id= ", id "\n name= ",name+"\n price:- ", str(price) ,"\n availability:- ",availability)



def updateSnacks():
    id=int(input("Enter snack Id"))

    flag=False 
    for i in list:
        if i["id"]==id:
            flag=True 
            price=int(input("Enter the Snack Price:- "))
            i["price"]=price

    if flag:
        print("Snacks Updated ")
    else:
        print("Snack Id Not preset in database")



def removeSnacks():
    id=int(input("Enter snack Id"))

    flag=False 
    for i in list:
        if i["id"]==id:
            flag=True 
            list.remove(i)

    if flag:
        print("Snacks Remove Successfully...")
    else:
        print("Snacks not present in this Snacks id")            
