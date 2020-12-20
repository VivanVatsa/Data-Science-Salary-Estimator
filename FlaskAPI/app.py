import flask
from flask import Flask, jsonify, request
import json
from flask.helpers import get_debug_flag

app = Flask(__name__)


def load_models():
    file_name = "models/model_file.p"
    with open(file_name, "rb") as pickled:
        data = pickle.load(pickled)
        model = data["model"]
    return model


@app.route("/predict", methods=["GET"])
def predict():
    response = json.dumps({"response": "freak-yeahhh"})
    return response, 200


if __name__ == "__main__":
    application.run(debug=True)
