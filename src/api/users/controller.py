from flask_restful import Resource, request

users = []

# @app.route('/users/<string:name>)
class User(Resource):
  def get(self, name):
    user = next(filter(lambda x: x['name'] == name, users), None)
    return {'status': True, 'message': '', 'data': user}, 200 if user else 400

  def post(self, name):
    if(next(filter(lambda x: x['name'] == name, users), None)):
      return {'status': False, 'message': 'An user with name \'{}\' already exists'.format(name)}, 400

    data = request.get_json()
    user = {'name': name, 'email': data['email']}
    users.append(user)
    return {'status': True, 'message': 'User created', 'data': user}, 201

  def put(self, name):
    data = request.get_json()
    user = next(filter(lambda x: x['name'] == name, users), None)

    if user is None:
      user = {'name': name, 'email': data['email']}
      users.append(user)
      return {'status': True, 'message': 'User Created', 'data': user}, 201

    user.update(data)
    return {'status': True, 'message': 'User Updated', 'data': user}, 201

  def delete(self, name):
    global users
    users = list(filter(lambda x: x['name'] != name, users))
    return {'status': True, 'message': 'User deleted', 'data': []}, 201

# @app.route('/users)
class UserList(Resource):
  def get(self):
    return {'status': True, 'message': '', 'data': users}, 200
