from flask import Flask, request, jsonify



app = Flask(__name__)
@app.route('/daniya')
def daniya():
    return 'ehg'

@app.route('/dan')
def dsf():
 return 'asdf'

app.run()