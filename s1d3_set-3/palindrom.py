input="madam"

i=0
j=len(input)-1

flag=True

while(i<=j):
    if input[i]!=input[j]:
        flag=False
        break
    else:
        i+=1
        j-=1

if flag:
    print("The word "+input+" is a palindrome.")
else:
     print("The word "+input+" is not a palindrome.")   
