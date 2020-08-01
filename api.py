#!flask/bin/python
from flask import Flask, jsonify
from flask import request
import ai as aI

app = Flask(__name__)

@app.route('/sense/<message>',methods=['GET'])
def index(message):
    result = aI.getMood(message)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)