from flask import Flask, render_template, jsonify
from faker import Faker

import uuid

app = Flask(__name__)
fake = Faker()

users = []
for _ in range(10): 
  id =  str(uuid.uuid4())
  name = fake.name()
  address = fake.address()
  phone = fake.phone_number()
  user = {"id": id, "name": name, "address": address, "phone": phone }
  users.append(user)

@app.route('/')
def hello_world():
  return render_template('hello.html')

@app.route('/users/')
def get_users():
  return jsonify(users)
  
@app.route('/users/<id>')
def get_by_id(id = None):
  for user in users:
    if(user["id"] == id):
      return jsonify(user)
    pass  

  return jsonify({"message": "User not found"})