#  ID, dish name, price, and availability (yes or no).

class Dish:

    def __init__(self,id,name,price,availability):
        self.id=id
        self.name=name
        self.price=price
        self.availability=availability
        # self.status=status
        

    def print(self):
        print("Dish id:- "+str(self.id))
        print("Dish name:- "+self.name)
        print("Dish price:- "+str(self.price))
        print("Dish availability:- "+self.availability)  
        # print("Disk status:- "+self.status)  

dish1=Dish(1,"Samosa",32,"yes")
dish2=Dish(2,"Paratha",60,"yes")
dish3=Dish(3,"Chilly",70,"yes")
dish4=Dish(4,"Momos",30,"yes")
dish5=Dish(5,"Barger+chhiji",40,"yes")

dishs=[]


dishs.append(dish1)
dishs.append(dish2)
dishs.append(dish3)
dishs.append(dish4)
dishs.append(dish5)


orders=[]
def addDish():
    name=input("Enter Name...")
    price=int(input("Enter Price:- "))
    
    
    length=len(dishs)-1
    intid=dishs[length].id+1
    newdish=Dish(intid,name,price,"yes")
    # print(newdish)
    dishs.append(newdish)
    newdish.print()

def removeDish():
    try:
        idstr=input("enter the Dish id")
        id=int(idstr)
        flag=True
        for i in dishs:
            if id==i.id:
                # print("inside the if ")
                dishs.remove(i)
                print(i.print()," remove Successfully Done")
                flag=False
        if flag:        
            print(" Id not match")         
    except  ValueError:
        print(idstr+" can not convert into Integer")  

def updateAvailablity():
    try:
        idstr=input("enter the Dish id")
        id=int(idstr)
        flag=True
        for i in dishs:
            if id==i.id:
                i.availability="no"
                print(i.print()," updation Successfully Done")
                flag=False
        if flag:        
            print(" Id not match")        
    except  ValueError:
        print(idstr+" can not convert into Integer") 
             


def takeOrder():
    try:
        idstr=input("enter the Dish id")
        id=int(idstr)
        flag=True
        for i in dishs:
            if id==i.id:
                if i.availability=="yes":
                    flag=False
                    quantity=int(input("enter The Quantity"))
                    order=(i,quantity,"received")
                    orders.append(order)
                    print(order)

                
        if flag:        
            print(" Id not match")        
    except  ValueError:
        print("String can not convert into Integer") 

def updateStatus():    
       for i in orders:
           print(i[2])
           i[2]="preparing"
    # for i in range(0,len(orders)):
    #     order=orders[i]
    #     print(order)
    #     if order[2]=="delivered":
    #         continue
    #     elif order[2]=="preparing":
    #         # order[2]="delivered"
    #         # orders[i+1][2]="preparing"
    #         order[0].print()
    #         order[2]
    #         break
    #     else:
    #         if order[2]=="received":
    #                 #   order[2]="preparing"
    #                   order[0].print()
    #                   order[2]            
                      

def reviewAllTheOrder():
    for i in orders:
        i[0].print()
        print(i[1])
        print(i[2])

def exit():
    print("Thanks for Services")

def viewDishs():
    for i in dishs:
        i.print()
        print("===================================")



choice=1

while choice!=0:
    print("1:- Add Delicious new Disk ")
    print("2:-Remove if Not Present")
    print("3:-Update availability")
    print("4:-Take Order")
    print("5:- update the status")
    print("6:-Review All the orders")
    print("7:-view  all the Dishs ")
    print("0:-for Exit")
    try:
       inpu=input("Enter your choice:- ")
       choice=int(inpu)
       
       if choice==1:
           addDish()
       elif choice==2:
           removeDish()
       elif choice==3:
           updateAvailablity()
       elif choice==4:
           takeOrder()
       elif  choice==5:
           updateStatus()
       elif choice==6:
           reviewAllTheOrder()
       elif choice==7:
           viewDishs()    
       elif choice==0:
           exit()
       else:
           print("enter Valid Number")    
                                



    except ValueError:
        print(inpu+" can not convert into Integer1") 
    except Exception as e:
        print("System error is:- "+str(e))    


