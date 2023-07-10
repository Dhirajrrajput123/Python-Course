
num=1
print("welcome our application")
while num!=0:
    str=input("Enter the String")
    rev=""
    for i in str:
        
        rev=i+rev

    print(rev)

    num=int(input("enter 0 for exit\n enter 1 for continue"))

print("thanks for using out application")        