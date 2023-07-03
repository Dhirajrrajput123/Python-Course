x=0

try:
    result=120/x

except ZeroDivisionError:
    print("print: Division by Zero is not allowed")

except Exception as e:
    print("An error occured:", str(e))

finally:
    print("Finally block executed")

print("program complete")