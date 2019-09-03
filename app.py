from flask import Flask
from src.routing.setup import init_routes

app = Flask(__name__)
app.secret_key = '21312dn1dn93y4h1b1vf1f81y87y123sb'

# routes
init_routes(app)

app.run(port=5000)
