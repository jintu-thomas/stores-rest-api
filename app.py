import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from resources.item import Item,ItemList
from security import authentcate,identity 
from resources.user import UserRegister
from resources.stores import Store,StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

# @app.before_first_request                   
# def create_tables():
#     db.create_all()   #(this is for run locallly otherwise run.py)


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