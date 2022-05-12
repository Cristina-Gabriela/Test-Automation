
import requests
from flask import Flask, jsonify, request

server_port = 5000

app = Flask(__name__)
app.config["DEBUG"] = True

users = [{
    "name": "Cristina",
    "email": "raileanu.cristina91@gmail.com",
    "phone": "0754945645"
},
    {
        "name": "Gabriela",
        "email": "raileanu.cristina91@gmail.com",
        "phone": "0754945645"
    }
]


@app.route("/")
def get_user():
    return users[0]


@app.route("/users")
def get_user():
    return jsonify({
        "users": users
    })


@app.route("/users", methods=["POST"])
def add_user():
    usr = request.get_json()
    for user in users:
        if user['email'] == usr['email']:
            return f"The user {usr['email']} is already registered!", 200
        else:
            users.append(usr)
            return "User added", 201


@app.route("/users", methods=["DELETE"])
def delete_user():
    usr = request.get_json()
    for user in users:
        if user['email'] == usr['email']:
            users.remove(user)
            return f"The user {usr['email']} has been remouved!", 204
    else:
        return "The user was not found.", 404


if __name__ == '__main__':
    app.run("localhost", port=server_port, debug=True)



# TODO : PUT o tema pentru acasa