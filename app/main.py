from flask import Flask, request
from flask_cors import CORS
from flasgger import Swagger
from remlapreprocesspy import preprocess
from tensorflow.keras.models import load_model

app = Flask(__name__) 
swagger = Swagger(app)
cors = CORS(app)

model = load_model("models/phishing_model.keras")

@app.route('/querymodel', methods=['POST']) 
def predict():
    """
    Make a prediction through latest phishing model about given urls 
    ---
    consumes:
        - application/json
    parameters:
        - name: urls
          in: body
          description: List of URLs to be classified
          required: True
          schema:
            type: object
            required: urls
            properties:
              urls:
                type: array
                items:
                  type: string
                example: ["http://www.example.com","http://example.org"]
    responses:
      200:
        description: Successfully processed the URLs. The response contains an array of results, with each item providing details about the classification of a URL. Each item includes whether the URL is classified in a specific category (true or false), the probability of that classification, and the URL itself.
        content:
        application/json:
          schema:
            type: object
            properties:
              results:
                type: array
                items:
                  type: object
                  properties:
                    classification:
                      type: boolean
                      description: Indicates whether the URL is classified in the specified category. 'False' means it does not meet the criteria for the category.
                    probability:
                      type: number
                      format: float
                      description: The probability score between 0 and 1, indicating the confidence of the classification decision.
                    url:
                      type: string
                      description: The URL that was evaluated."""

    threshold = 0.7

    urls = request.get_json().get('urls')
    tokenized = preprocess(urls)

    #Returns list of lists [[res_1],[res_2],...]
    raw_query_result = model.predict(tokenized)
    print(raw_query_result)
    query_result = raw_query_result.tolist()
     # Generate responses: {results: [{url: url1, classification: true, probability: 0.34}]} for example
    query_reponse = {"results": [{"url": urls[i], 
                                  "classification": query_result[i][0] > threshold, 
                                  "probability": query_result[i][0]}                for i in range(len(urls))]}
    return query_reponse
    #return { "result": [i[0] > threshold for i in query_result], "probabilities": [i[0] for i in query_result]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=False)