
name="jarihD"

namrcorrect= name[::-1]
print(namrcorrect)

nameloop=""
for i in range(len(name) - 1, -1, -1):
    nameloop+=name[i]

print(nameloop)    