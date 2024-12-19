import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import encode_sample

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument("age")
parser.add_argument("gender")
parser.add_argument("category")
parser.add_argument("purchaseAmount")
parser.add_argument("season")
parser.add_argument("reviewRating")
parser.add_argument("subscriptionStatus")
parser.add_argument("discountApplied")
parser.add_argument("previousPurchases")
parser.add_argument("frequencyOfPurchases")


validate_model = pickle.load(open("./model_customer.pckl", "rb"))


class ValidationEndPoint(Resource):
    def get(self):
        url_features = [[25, 0, 1, 150.0, 3, 4.5, 1, 10, 3, 2]]
        predict_value = validate_model.predict(url_features)
        print(predict_value[0])
        return {"hello": "world"}

    def post(self):
        args = parser.parse_args()
        age = args.get("age")
        gender = args.get("gender")
        category = args.get("category")
        purchaseAmount = args.get("purchaseAmount")
        season = args.get("season")
        reviewRating = args.get("reviewRating")
        subscriptionStatus = args.get("subscriptionStatus")
        discountApplied = args.get("discountApplied")
        previousPurchases = args.get("previousPurchases")
        frequencyOfPurchases = args.get("frequencyOfPurchases")

        print(age)
        url_features = [
            age,
            gender,
            category,
            purchaseAmount,
            season,
            reviewRating,
            subscriptionStatus,
            discountApplied,
            previousPurchases,
            frequencyOfPurchases,
        ]
        url_features = [
            int(feature) if feature is not None else 0 for feature in url_features
        ]
        print(url_features)

        predict_value = validate_model.predict([url_features])
        print("Bo may den day : ", predict_value[0])

        # return {
        #     "result": predict_value[0],
        # }
        return (
            {
                "result": "Potential Customer",
            }
            if predict_value[0] == 1
            else {
                "result": "Not Potential Customer",
            }
        )


api.add_resource(ValidationEndPoint, "/api/v1/predict")

if __name__ == "__main__":
    app.run(debug=True)
