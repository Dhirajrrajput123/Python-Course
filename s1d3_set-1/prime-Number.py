
num=19990


flag=True

for i in range(2,int(num/2)+1):
    if num%i==0:
        flag=False
        break

if flag:
    print(num," is a prime number")
else:
    print(num," is not a prime number")
            