from flask import Flask, jsonify
app = Flask(__name__)

data = {
        "name" : "young",
        "age" : 15,
        "location" : "seoul"
    }
@app.route("/data")
def just_data():
    return data
@app.route("/data/json")
def json_data():
    return jsonify(data)