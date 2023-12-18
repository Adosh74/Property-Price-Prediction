from django.shortcuts import render
import os
# ML model packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def home(request):
    return render(request, 'home.html')


def predict(request):
    return render(request, 'predict.html')

def result(request):

    try: 

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # for production (linux)
        # data = pd.read_csv(os.getcwd() + "/" + "server" + "/" +  "USA_Housing.csv")

        # for development (windows)
        data = pd.read_csv(os.getcwd() + "\\" + "server" + "\\" +  "USA_Housing.csv")
        
        # get the working directory path

        

        data = data.drop(['Address'], axis=1)

        X = data.drop('Price', axis = 1)
        Y = data['Price']
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .30, random_state=123)

        model = LinearRegression()
        model.fit(X_train, Y_train)

        value1 = float(request.GET['n1'])
        value2 = float(request.GET['n2'])
        value3 = float(request.GET['n3'])
        value4 = float(request.GET['n4'])
        value5 = float(request.GET['n5'])

        prediction = model.predict(np.array([value1, value2, value3, value4, value5]).reshape(1, -1))
        prediction = round(prediction[0])

        price = "The price of the house is: " + str(prediction) + "$"
        if(prediction > 0):
            return render(request, 'result.html', {'result2': price})
        return render(request, 'result.html', {'result2': 'use valid input'})
    except: 
        price = "use valid input"
        return render(request, 'result.html', {'result2': price})