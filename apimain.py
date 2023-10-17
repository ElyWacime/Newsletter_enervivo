from flask import Flask, request, jsonify

app = Flask(__name__)
stored_payload = None

@app.route('/store', methods=['POST'])
def store_json():
    global stored_payload
    json_data = request.get_json()
    stored_payload = json_data
    return "JSON payload stored successfully", 200

@app.route('/get', methods=['GET'])
def get_json():
    if stored_payload is not None:
        return jsonify(stored_payload), 200
    else:
        return "No JSON payload stored", 404

if __name__ == '__main__':
    app.run(debug=True)
