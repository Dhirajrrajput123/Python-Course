from flask import Flask,render_template, jsonify, request

app = Flask(__name__)


class Product():

    def __init__(self, id, name, price, availability):
        self.id = id
        self.name = name
        self.price = price
        self.availability = availability

    def printproduct(self):
        print("product detail is:- ", self.id, self.name, self.price, self.availability)


class Order():

    def __init__(self, oId, product, cName, status):
        self.oId = oId
        self.product = product
        self.cName = cName
        self.status = status


list = []
product1 = Product(1, "Sugar", 45, "yes")
product2 = Product(2, "Chai", 299, "yes")
product3 = Product(3, "Shope", 120, "yes")
product4 = Product(4, "kurkure", 30, "yes")
product5 = Product(5, "chatpata", 20, "yes")

list.append(product1)
list.append(product2)
list.append(product3)
list.append(product4)
list.append(product5)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/products', methods=['GET'])
def getAllProducts():
    # result = []
    # for i in list:
    #     product = {}
    #     product['id'] = i.id
    #     product['name'] = i.name
    #     product['price'] = i.price
    #     product['availability'] = i.availability
    #     result.append(product)
    print(list)
    return render_template('displatall.html', list=list )


@app.route('/products/<pId>', methods=['GET'])
def getproduct(pId):
    for i in list:
        if i.id == int(pId):
            product = {}
            product['id'] = i.id
            product['name'] = i.name
            product['price'] = i.price
            product['availability'] = i.availability
            return jsonify(product)

    return jsonify({'message': 'Product not present in this id '})


@app.route('/products', methods=['POST'])
def addProducts():
    id = list[len(list) - 1].id + 1
    name = request.form['name']
    price = request.form['price']
    availability =request.form['availability']
    product = Product(id, name, price, availability)
    list.append(product)
    return render_template('displatall.html', list=list )


@app.route('/products/<int:pId>', methods=['PUT'])
def addProduct(pId):
    price = request.json['price']
    availability = request.json['availability']
    for i in list:
        if i.id == pId:
            i.price = price
            i.availability = availability
            return jsonify({'message': 'Product updated successfully'})
    return jsonify({'message': 'product not present in this product id'})

@app.route('/product/update/<int:pId>',methods=['GET'])
def updateprodu(pId):
    for i in list:
        if i.id == pId:
            if i.availability=='yes':
                i.availability='no'
            else:
                i.availability='yes'
            return render_template('displatall.html', list=list )
    return jsonify({'message': 'product not present int this id'})

@app.route('/products/delete/<int:pId>', methods=['GET'])
def deleteProduct(pId):
    for i in list:
        if i.id == pId:
            list.remove(i)
            return render_template('displatall.html', list=list )
    return jsonify({'message': 'product not present int this id'})


ordersList = []


@app.route("/orders", methods=['POST'])
def newOrder():
    productId = request.form['pid']
    productId=productId.strip()
    cName = request.form['cName']
    #  status=request.json['status']
    print(productId)
    pIds = productId.split(" ")
    orderProduct = []
    for j in pIds:
        flag = False
        pd = list[0]
        for i in list:
            pd = i
            if i.id == int(j):
                orderProduct.append(i)
                pd = i
                flag = True
                break
        if flag == False:
            return jsonify({'id': pd.id, 'name': pd.name, 'message': "this product no longer present"})
    oid = len(ordersList) + 1

    order = Order(oid, orderProduct, cName, "received")
    ordersList.append(order)
    return render_template('order.html', ordersList=ordersList )


@app.route('/order/<int:oId>', methods=['GET'])
def getOrder(oId):
    print(type(oId))
    for i in ordersList:
        if i.oId == int(oId):
            pd = []
            for j in i.product:
                pd.append({'id': j.id, 'name': j.name, 'price': j.price})
            return jsonify({'id': oId, 'product': pd})
    print("jcjhdfb")
    return jsonify({'message': 'Product not Present'})


@app.route('/orders', methods=['GET'])
def getOrders():
    orders = []
    # for i in ordersList:
    #     order = {}
    #     order['id'] = i.oId
    #     #   order['product']=i.product
    #     order['name'] = i.cName
    #     order['status'] = i.status
    #     orders.append(order)
    print(ordersList)
    return render_template('order.html', ordersList=ordersList )


@app.route('/orders/update/<int:oId>', methods=['GET'])
def updateOrder(oId):
    # status = request.json['status']

    for i in ordersList:
        if i.oId == oId:
            if i.status=="received":
                i.status="preparing"
            elif i.status=="preparing":
                i.status="delivered"
            else:
                i.status="delivered"
            return render_template('order.html', ordersList=ordersList )

    return jsonify({'message': 'Invalid Order Id'})


if __name__ == '__main__':
    app.run()