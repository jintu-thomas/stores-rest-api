import os


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from resources.item import Item,ItemList
from security import authentcate,identity 
from resources.user import UserRegister
from resources.stores import Store,StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://ynyesrayzkhjog:77418e3b58fa64f4b1fe892982f0dd4e3048472ac29ca0a8f120f3f3a419a309@ec2-54-73-68-39.eu-west-1.compute.amazonaws.com:5432/d4383tu71jljj','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)



jwt = JWT(app,authentcate,identity)         #jwt create new endpoint calle s /auth`



api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(ItemList,'/items')
api.add_resource(Item,'/item/<string:name>')          #https://127.0.0.1:5000/sttudent/jintu
api.add_resource(UserRegister, '/register')

if __name__=='__main__':
    from db import db
    db.init_app(app)        #circular imports
    app.run(port = 5000,debug=True)