from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"name": "Andrei", "age": 29},
    {"name": "John", "age": 23},
    {"name": "Bob", "age": 34}
]

@app.route("/user/<name>", methods=["PATCH"])
def update_user_age(name):
    for user in users:
        if user["name"] == name:
            user["age"] = request.json["age"]
            return jsonify(user)
    return jsonify({"message": "User not found"})

if __name__ == '__main__':
    app.run(debug=True)