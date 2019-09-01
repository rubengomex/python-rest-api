from flask_restful import Resource, Api, request
from api.users.controller import User, UserList
from auth import configure_auth

def routing(app):
  api = Api(app)

  # auth routes /auth
  configure_auth(app)
  # users routes /users
  api.add_resource(UserList, '/users/')
  api.add_resource(User, '/users/<string:name>/')
