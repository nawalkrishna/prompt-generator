from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Python backend is working!", "status": "success"})
