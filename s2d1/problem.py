from flask import Flask, jsonify, request
app = Flask(__name__)

class Product():

    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

    def printproduct(self):
        print("product detail is:- ",self.id,self.name,self.price)

list=[]
product1=Product(1,"Sugar",45)
product2=Product(2,"Chai",299)
product3=Product(3,"Shope",120)
product4=Product(4,"kurkure",30)
product5=Product(5,"chatpata",20)

list.append(product1)
list.append(product2)
list.append(product3)
list.append(product4)
list.append(product5)

@app.route('/')
def hello_world():
    return 'Hello,! how can i help you'

@app.route('/products',methods=['GET'])
def getAllProducts():
    result=[]
    for i in list:
        product={}
        product['id']=i.id
        product['name']=i.name
        product['price']=i.price
        result.append(product)
    return jsonify(result)


@app.route('/products/<pId>',methods=['GET'])
def getproduct(pId):
        
        for i in list:
             if i.id==int(pId):
                  product={}
                  product['id']=i.id
                  product['name']=i.name
                  product['price']=i.price
                  return jsonify(product)
        
        return jsonify({'message':'Product not present i this id '})


@app.route('/products',methods=['POST'])
def addProducts():
     id=list[len(list)-1].id+1
     name=request.json['name']
     price=request.json['price']
     product=Product(id,name,price)
     list.append(product)
     return jsonify({'message':'product added successfully'})


@app.route('/products/<int:pId>',methods=['PUT'])
def addProduct(pId):
     price=request.json['price']

     for i in list:
          if i.id==pId:
               i.price=price
               return jsonify({'message':'Product updated successfully'})
     return jsonify({'message':'product not present in this product id'})

@app.route('/products/<int:pId>',methods=['DELETE'])
def deleteProduct(pId):
     for i in list:
          if i.id==pId:
               list.remove(i)
               return jsonify({'message':'Product deleted successfully'})
     return jsonify({'message':'product not present in this id'})     
     
   
if __name__ == '__main__':
    app.run(port=5001)