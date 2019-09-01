from flask import Flask
from routing import routing

app = Flask(__name__)
app.secret_key = '21312dn1dn93y4h1b1vf1f81y87y123sb'

# routes
routing(app)

app.run(port=5000)
