from flask_restful import Resource, Api, request
from ..api.users.controller import User, UserList
from ..auth.setup import configure_auth

def init_routes(app):
  api = Api(app)

  # auth routes /auth
  configure_auth(app)
  # users routes /users
  api.add_resource(UserList, '/users/')
  api.add_resource(User, '/users/<string:id>/')
