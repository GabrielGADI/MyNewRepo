from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

cars_file = "cars.csv"
cars = []

@app.before_first_request
def load_cars():
    with open(cars_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cars.append(row)

@app.route("/cars", methods=["GET"])
def get_cars():
    return jsonify(cars)

@app.route("/cars", methods=["POST"])
def create_car():
    car = request.json
    cars.append(car)
    with open(cars_file, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=car.keys())
        writer.writerow(car)
    return jsonify(car)

@app.route("/cars/<int:year>", methods=["PATCH"])
def update_car(year):
    for car in cars:
        if int(car["year"]) == year:
            car.update(request.json)
            with open(cars_file, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=car.keys())
                writer.writeheader()
                writer.writerows(cars)
            return jsonify(car)
    return jsonify({"message": "Car not found"})

@app.route("/cars/<int:year>", methods=["DELETE"])
def delete_car(year):
    for car in cars:
        if int(car["year"]) == year:
            cars.remove(car)
            with open(cars_file, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=car.keys())
                writer.writeheader()
                writer.writerows(cars)
            return jsonify({"message": "Car deleted"})
    return jsonify({"message": "Car not found"})

if __name__ == '__main__':
    app.run(debug=True)