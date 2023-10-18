from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/store', methods=['POST'])
def store_json():
    specific_key = request.args.get("key")

    json_data = request.get_json()

    with open("data.json", "a") as file:
        data_to_store = {specific_key: json_data}
        json.dump(data_to_store, file)
        file.write("\n")

    return "JSON payload stored successfully", 200

@app.route('/get', methods=['GET'])
def get_json():
    data = []

    try:
        with open("data.json", "r") as file:
            for line in file:
                data.append(json.loads(line))
        return jsonify(data), 200
    except FileNotFoundError:
        return "No JSON payload stored", 404

if __name__ == '__main__':
    app.run(debug=True)
