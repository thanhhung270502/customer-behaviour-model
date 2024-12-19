import pickle
import numpy as np
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import encode_sample

column_replacements = {
    'Frequency of Purchases': (['Annually', 'Every 3 Months', 'Quarterly', 'Monthly', 'Bi-Weekly', 'Fortnightly', 'Weekly'], [0, 1, 1, 2, 3, 3, 4]),
    'Discount Applied': (['Yes', 'No'], [1, 0]),
    'Promo Code Used': (['Yes', 'No'], [1, 0]),
    'Gender': (['Male', 'Female'], [1, 0]),
    # 'Shipping Type': (['Standard', 'Free Shipping', 'Next Day Air', 'Express', '2-Day Shipping', 'Store Pickup'], [1, 2, 3, 4, 5, 6]),
    'Subscription Status': (['Yes', 'No'], [1, 0]),
    'Season': (['Summer', 'Fall', 'Winter', 'Spring'], [1, 2, 3, 4]),
    'Category': (['Clothing', 'Footwear', 'Accessories', 'Outerwear'], [1, 2, 3, 4]),
    'Size': (['L', 'S', 'M', 'XL'], [1, 2, 3, 4]),
    'Payment Method': (['Credit Card', 'Bank Transfer', 'Cash', 'PayPal', 'Venmo', 'Debit Card'], [1, 2, 3, 4, 5, 6]),
    # 'Preferred Payment Method': (['Credit Card', 'Bank Transfer', 'Cash', 'PayPal', 'Venmo', 'Debit Card'], [1, 2, 3, 4, 5, 6])
}

url_features = {
    'Age': 25,
    'Gender': 0,
    'Category': 1,
    'Purchase Amount (USD)': 150.0,
    'Season': 3,
    'Review Rating': 4.5,
    'Subscription Status': 1,
    'Discount Applied': 10,
    'Previous Purchases': 3,
    'Frequency of Purchases': 2

}
X = np.array([list(url_features.values())]) 


validate_model = pickle.load(open('./model_customer.pckl', 'rb'))
predict_value = validate_model.predict(X)
print( "Bo may den day : " , predict_value[0])