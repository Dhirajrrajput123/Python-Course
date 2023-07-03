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
    print(newSnack)



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


def printList():
   for i in list:
      print(i)

choice=1
while choice!=0:
    try:
      choice=int(input("Enter your choice:- \n 1:- add snack. \n 2:- update Snack \n 3:- delete Snack \n 4:- display all Snacks \n   0:- for Exit"))
      if choice==1:
        addSnacks()
      elif choice==2:
        updateSnacks()
      elif choice==3:
        removeSnacks()   
      elif choice==0:
        print("Thanks Our Services")
      elif choice==4:
        printList();  
      else:
        print("Please enter valid Number") 
    except Exception:
       print("can not convert into Integer")
       
    

