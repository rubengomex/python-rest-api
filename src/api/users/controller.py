from flask_restful import Resource, request, reqparse
from .model import UserModel
import sqlite3


# @app.route('/users/)
class User(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('email',
                      type=str,
                      required=True,
                      help='Email cannot be blank'
                      )
  parser.add_argument('password',
                      type=str,
                      required=True,
                      help='Password cannot be blank'
                      )

  def post(self):
    data = User.parser.parse_args()

    if UserModel.find_by_email(data['email']):
      return {'status': False, 'message': 'An user with that email already exists'}, 400

    UserModel.create(data['email'], data['password'])

    return {'status': True, 'message': 'User created', 'data': list()}, 201

  def delete(self, id):
    if not UserModel.find_by_id(_id=id):
      return {'status': True, 'message': 'User has been removed'}, 200

    UserModel.remove(_id=id)
    return {'status': True, 'message': 'User has been removed'}, 200


# @app.route('/users)
class UserList(Resource):
  def get(self):
    return {'status': True, 'message': '', 'data': UserModel.find_all()}, 201
