from flask import Flask, request
from flasgger import Swagger
from lib import preprocess

from tensorflow.keras.models import load_model

app = Flask(__name__) 
swagger = Swagger(app)

@app.route('/', methods=['POST']) 
def predict():
    """
    Make a hardcoded prediction ---
    consumes:
    - application/json parameters:
    - name: input_data in: body
    description: message to be classified. required: True
    schema:
    type: object required: sms properties:
    responses: 200:
    msg:
    type: string
    example: This is an example msg.
    description: Some result """

    urls = request.get_json().get('urls')
    tokenized = preprocess(urls)
    raw_query_result = model.predict(tokenized)
    print(raw_query_result)
    return { "result": raw_query_result.tolist() }

if __name__ == "__main__":
    model = load_model("app/phishing_model.keras")
    app.run(host="0.0.0.0", port=8080, debug=True)