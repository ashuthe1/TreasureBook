from flask import Flask, request, jsonify
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://mongodb-service:27017/")  # Kubernetes service name
db = client.treasurebook

@app.route('/node', methods=['POST'])
def create_node():
    data = request.json
    collection = db.nodes
    node_id = collection.insert_one(data).inserted_id
    return jsonify({"message": "Node created", "node_id": str(node_id)}), 201

@app.route('/edge', methods=['POST'])
def create_edge():
    data = request.json
    collection = db.edges
    edge_id = collection.insert_one(data).inserted_id
    return jsonify({"message": "Edge created", "edge_id": str(edge_id)}), 201

@app.route('/nodes', methods=['GET'])
def get_nodes():
    collection = db.nodes
    nodes = list(collection.find({}, {"_id": 0}))
    return jsonify(nodes)

@app.route('/edges', methods=['GET'])
def get_edges():
    collection = db.edges
    edges = list(collection.find({}, {"_id": 0}))
    return jsonify(edges)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
