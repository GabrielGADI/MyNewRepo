from flask import Flask, jsonify, abort, request

from Sesiunea12.users_app.users_repo import UsersRepo

app = Flask(__name__)
user_repo = UsersRepo("./users.csv")


# deschidem fisierul si returnam continutul in format json
@app.route("/users")
def get_all():
    users = user_repo.read()
    return jsonify(users)  # importam jsonify si trimitem lista in format json


'''
in clientul ARC alegem metoda GET pentru a trimite toate datele din users.csv, si
 Address url:http://127.0.0.1:5001/users

'''


@app.route("/users/<name>")
def find_one(name):
    user = user_repo.find_one(name)
    if user:
        return jsonify(user)
    abort(404, "user not found")  # importam abort


'''
in clientul ARC alegem metoda GET pentru a trimite toate datele din users.csv, si 
Address url:http://127.0.0.1:5001/users/Andrei
'''


@app.route("/users", methods=["POST"])
def add_user():
    user_repo.create(request.json)  # importam request
    return "ok", 201


'''
in clientul ARC alegem metoda POST pentru a trimite toate datele in users.csv, si
 Address url:http://127.0.0.1:5001/users si in Body adaugam "name": "x", "age": x

'''

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # putem schimba portul
