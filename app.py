import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from resources.item import Item,ItemList
from security import authentcate,identity 
from resources.user import UserRegister
from resources.stores import Store,StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://ntqnidwrbnqzbc:5841b1bea93df70149a5b81b3c6cb78791b41a463ce8ab10c8a6bce1231685b7@ec2-54-74-60-70.eu-west-1.compute.amazonaws.com:5432/d5ahjmhblbc3e2')
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