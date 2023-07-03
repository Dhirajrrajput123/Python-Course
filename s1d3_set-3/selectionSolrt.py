input=[64,25,12,22,11]

for i in range(0,len(input)-1):
    index=i
    for j in range(i+1,len(input)):
        if input[index]>input[j]:
               index=j

    temp=input[i]
    input[i]=input[index]
    input[index]=temp

print(input)             

               