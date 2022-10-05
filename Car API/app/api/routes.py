from flask import Flask
app = Flask(__name__)


from urllib import response
from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Contact, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/user_posts', methods = ['POST'])
@token_required
def create_contact(current_user_token):
    print("comin here")
    name = request.json['username']
    email = request.json['email']
    user_token = current_user_token.token
    print(name)
    print(f'BIG TESTER: {current_user_token.token}')
    
    user_posts = Contact(email,name,user_token)
    
    db.session.add(user_posts)
    db.session.commit()
    
    response = contact_schema.dump(user_posts)
    return jsonify(response)