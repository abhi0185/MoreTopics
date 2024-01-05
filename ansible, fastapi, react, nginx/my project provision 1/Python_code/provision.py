from flask import Flask, jsonify, request

from flask_cors import CORS
app = Flask(__name__)
CORS(app)
#app = Flask(__name__)

@app.route('/regions', methods=['GET'])
def get_regions():
    regns = [
    {
        "code": "af-south-1",
        "name": "Africa: Cape Town",
        "description": "Africa (Cape Town) Region",
        "is_active": 0,
        "create_date": "2023-10-12 04:58:13"
    },
    {
        "code": "ap-south-1",
        "name": "Asia Pacific: Mumbai",
        "description": "Asia Pacific (Mumbai) Region",
        "is_active": 0,
        "create_date": "2023-10-12 04:58:13"
    }]
    return jsonify({'Regions': regns})

@app.route('/environments', methods=['GET'])
def get_environments():
    envsn = [
    {
        "id": "0x000D9F085D7C440B897D0695E218A6E3",
        "name": "aut entr dev0002 170",
        "status": "decommissioned",
        "region_code": "US: Virginia",
        "kony_account_id": 100000059,
        "create_date": "2023-11-20 05:01:14",
        "is_env_disabled": 0,
    },
    {
        "id": "0x001A4D233735451CA445CAE5934B4E3F",
        "name": "BVT-AUTHPAID-0e5d79",
        "status": "decommissioned",
        "region_code": "US: Virginia",
        "kony_account_id": 100000068,
        "create_date": "2023-11-20 05:01:14",
        "is_env_disabled": 0,
    }]
    return jsonify({'Environments': envsn})

# Route to add a new item to the database
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    name = data['name']
    description = data['description']

    cursor = db.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
    db.commit()
    cursor.close()

    return jsonify({'message': 'Item added successfully'})

# Route to delete an item from the database
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    db.commit()
    cursor.close()

    return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
