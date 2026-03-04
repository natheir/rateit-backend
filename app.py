from flask import Flask, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials

# Initialize Flask app
app = Flask(__name__)

# Setup CORS
CORS(app)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path/to/your/firebase-sdk.json')  # Update with your Firebase Admin SDK JSON path
firebase_admin.initialize_app(cred)

# Sample in-memory data for Restaurants and Dishes
restaurants = [
    {'id': 1, 'name': 'Restaurant A'},
    {'id': 2, 'name': 'Restaurant B'},
]

dishes = [
    {'id': 1, 'name': 'Dish A', 'restaurant_id': 1},
    {'id': 2, 'name': 'Dish B', 'restaurant_id': 1},
    {'id': 3, 'name': 'Dish C', 'restaurant_id': 2},
]

# Endpoint to get all restaurants
@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(restaurants), 200

# Endpoint to get all dishes
@app.route('/api/dishes', methods=['GET'])
def get_dishes():
    return jsonify(dishes), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)