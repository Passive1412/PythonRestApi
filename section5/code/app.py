from datetime import timedelta
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity as identity_function
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELT'] = timedelta(seconds=1800)
#app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
#app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity_function)

#@jwt.auth_response_handler
#def customized_response_handler(access_token, identity):
#    return jsonify({
#        'access_token': access_token.decode('utf-8'),
#        'user_id': identity.id
#    })

@jwt.jwt_error_handler
def customized_error_handler(error):
    return jsonify({
        'message': error.description,
        'code': error.status_code
    }). error.status_code

api.add_resource(Item, '/item/<string:name>') # host 0.0.0.0:5000 at 172.18.64.200:5000/student/Rolf
api.add_resource(ItemList, '/items') # host 0.0.0.0:5000 at 172.18.64.200:5000/student/Rolf
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)