
def max_salary_employee(list):
    max=0
    maxEMp=None
    # print(list[0]["name"])
    for i in list:
      if i["salary"]>max:
          max=i["salary"]
          maxEMp=i


    return maxEMp



listemp=[
   {"name":"john","salary":3000,"designation":"developer"},
   {"name":"Harry","salary":4000,"designation":"coder"},
   {"name":"jack","salary":4001,"designation":"web app"},
   {"name":"hella","salary":7323,"designation":"hardware"},
   {"name":"juri","salary":8322,"designation":"eng"}
]  

res=max_salary_employee(listemp)
print(res)
