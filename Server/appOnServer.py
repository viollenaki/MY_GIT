from flask import Flask, Request, jsonify, request
from collections import defaultdict

class Client:
    def __init__(self, name, password):
        self.name = name
        self.password = password

clients = {}




app = Flask(__name__)
@app.route('/reg_info')
def reg_info():
    name = request.args.get('name')
    if name in clients:
        return jsonify('TRUE')
    else:
        return jsonify('FALSE')




@app.route('/register')
def register():
    name = request.args.get('name')
    password = request.args.get('password')
    clients[name] = Client(name, password)
    return jsonify('SUCCESSFUL')


app.run()