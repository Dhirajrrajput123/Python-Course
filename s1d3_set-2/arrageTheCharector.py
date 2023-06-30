str1 = "PyNaTive"

lower=""
upper=""

char="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in str1:
    flag=True
    for j in char:
        if j==i:
            upper+=j
            flag=False

    if flag:
        lower+=i


print(lower+upper)               


