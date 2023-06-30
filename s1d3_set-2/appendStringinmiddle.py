
string="Ault"

name="Kelly"

length=len(string)

fulllname=""
for i in range(0,length):
    if(i==length/2):
        fulllname+=name+string[i]
    else:
        fulllname+=string[i]

print(fulllname)