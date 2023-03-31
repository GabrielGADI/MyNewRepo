from flask import Flask, request

'''flask - framework in python putem crea aplicatii web mici
- ca flask sa functioneze vom avea intotdeauna un fisier 'app'
'''
app = Flask(__name__)  # obiectul aplicatiei (app)


@app.route("/")  # routa radacina "/"
def index():
    return "ok"


@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"


# vom folosi ARC cu metoda POST si la BODY vom aduce modificarile dorite
@app.route("/login", methods=["POST"])
def login():
    print(request.method)
    print(request.json)
    return "ok"


if __name__ == '__main__':  # if specific aplicatiile care se lanseaza dintr-un fisier(main TAB)
    app.run(debug=True)  # deschide aplicatia
