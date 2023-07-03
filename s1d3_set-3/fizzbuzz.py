output="1"

for i in range(2,101):
    if i%3==0 and i%5==0:
        output+=", FizzBuzz"
    elif i%3==0:
        output+=", Fizz"
    elif i%5==0:
        output+=", Buzz"
    else:
        output+=", "+str(i)

print(output)