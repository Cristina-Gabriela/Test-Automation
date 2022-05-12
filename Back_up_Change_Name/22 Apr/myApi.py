from flask import Flask, jsonify, request

server_port = 5000
app = Flask(__name__)

app.config["Debug"] = True

users = [{
    "name": "Cris",
    "email": "raileanu.cristina91@gmail.com",
    "phone": "0754945645"
},
    {
        "name": "X",
        "email": "x.gmail.com",
        "phone": "0101232222"
    }
]


@app.route("/")
def get_users():
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
        if user["email"] != usr["email"]:
            users.append(usr)
            return "User added", 201
        else:
            return f"A user {usr['email']} is already registred !", 200


@app.route("/users", methods=["DELETE"])
def delete_user():
    usr = request.get_json()
    print(usr)
    return "User removed", 204


if __name__ == "__main__":
    app.run("localhost", port=server_port, debug=True)



    