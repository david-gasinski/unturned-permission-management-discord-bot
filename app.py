# This is a flask-restful app which provides api endpoints for the following functions
# - Add a user to a permission
# - Remove a user from a permission
# - Check if a user has a permission

# Imports 
from flask import Flask
from flask_restful import Resource, Api, reqparse
from util.xml_edit import Permissions, XML
from dotenv import load_dotenv
from os import getenv

# Flask app and setting up api
app = Flask(__name__)
api = Api(app)
load_dotenv()
parser = reqparse.RequestParser()
parser.add_argument('steamid')
parser.add_argument('permission')

# Setting up the permissions and .env data
filepath = getenv('PERMISSIONS')
# Load the permissions file
ref = XML(filepath) 
# Load the permissions class
permissions = Permissions(ref) 

# Api endpoint classes
# Adding Permissions
class addPermission(Resource):
    def post(self):
        args = parser.parse_args()
        success = permissions.addPermission(args['permission'], args['steamid'])
        return {'status': success }

# Removing Permissions
class removePermission(Resource):
    def post(self):
        args = parser.parse_args()
        success = permissions.removePermission(args['permission'], args['steamid'])
        return {'status': success }
    
# View permissions of a steamid
class viewPermission(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        data = permissions.retrievePermissions(args['steamid'])
        return {"message" : data}

# View all members of a given permission
class viewMembers(Resource):
    def post(self):
        args = parser.parse_args()
        data = permissions.retrieveMembers(args['permission'])
        members = []
        for member in data:
            members.append(member.text)
        return {"message" : members}
    
# Check if steamid has a permission
class checkPermission(Resource):
    def post(self):
        args = parser.parse_args()
        hasPermisson = permissions.checkPermission(args['permission'], args['steamid'])
        return {"message" : hasPermisson}
    
# Adding the api endpoints
api.add_resource(addPermission, '/add') # works
api.add_resource(removePermission, '/remove') # works
api.add_resource(viewPermission, '/view') # works
#api.add_resource(viewMembers, '/members')
api.add_resource(checkPermission, '/check') # works

if __name__ == '__main__':
    app.run(host="localhost", port=8000)