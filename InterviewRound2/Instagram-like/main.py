
from flask import Flask,request

app = Flask(__name__)

list=[]
@app.route("/")
def helloworld():
    return "hello world"


@app.route("/addPost"  , methods=['POST'])
def addpost():
    name=request.get_json("name")
    caption=request.get_json("caption")
    id=request.get_json(("id"))

    dis={
        "name":name,
        "caption":caption,
        "id":id,
        "like":0
    }
    list.append(dis)
    return "Post Upload successfully"

@app.route("/viewPost",methods=['GET'])
def getPost():
    newlist=[]
    for i in list:
        name=i["name"]
        caption=i["caption"]
        like=i["like"]
        id=i["id"]
        disc={
        "name":name,
        "caption":caption,
        "like":like,
        "id":id
        }
        newlist.append(disc)

    return jsonfy(newlist)



@app.route("/viewPost/<int:id>",methods=['DELETE'])
def delete(id):
    for i in list:
        if i["id"]=id:
            list.remove(i)
            break

    return "post deleted"





if __name__==__file__:
    app.run()
