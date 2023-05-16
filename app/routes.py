from flask import jsonify, request
from app import app, db
from bson import ObjectId


# Create a new record
@app.route('/todo/create', methods=['POST'])
def create_record():
    data = request.json
    db.todo.insert_one(data)
    return jsonify({'message': 'New todo created successfully'})

# Get all records


@app.route('/todo/list', methods=['GET'])
def get_records():
    records = list(db.todo.aggregate(
        [
            {
                "$project": {
                    "name": "$name",
                    "description": "$description",
                    "id": {"$toString": "$_id"},
                    "_id": 0
                }
            }
        ]
    ))

    return jsonify(records)

# Get a single record


@app.route('/todo/list/<id>', methods=['GET'])
def get_record(id):

    record = list(db.todo.aggregate(
        [
            {
                "$match": {
                  "_id": ObjectId(id)
                  }
            },
            {
                "$project": {
                    "name": "$name",
                    "description": "$description",
                    "id": {"$toString": "$_id"},
                    "_id": 0
                }
            }
        ]
    ))
    return jsonify(record)

# Update a record


@app.route('/todo/update/<id>', methods=['PUT'])
def update_record(id):
    data = request.json
    result = db.todo.update_one({'_id': ObjectId(id)}, {'$set': data})
    print(result)
    return jsonify({'message': 'Record updated successfully'})

# Delete a record


@app.route('/todo/delete/<id>', methods=['DELETE'])
def delete_record(id):
    db.todo.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Record deleted successfully'})
