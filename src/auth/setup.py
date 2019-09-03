from flask_jwt import JWT, jwt_required
from .security import authenticate, identity

def configure_auth(app):
  JWT(app, authenticate, identity)  # /auth
