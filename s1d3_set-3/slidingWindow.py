input=[2,15,11,7]
target=9
input.sort()
i=0
j=len(input)-1
# print(j)
while i<j:
      sum=input[i]+input[j]
      if sum>target:
            j-=1
      elif sum<target:
            i+=1
      else:
            print([i,j])
            break             
 


# print(input)