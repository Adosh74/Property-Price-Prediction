# Property-Price-Prediction
1. [Description](#description)
2. [Algorithm used](#algorithm-used)
3. [Server](#server)
4. [How to install and run the project](#how-to-install-and-run-the-project)
5. [How to use the project](#how-to-use-the-project)
6. [About the Model](#about-the-model)
7. [Screenshots](#screenshots)
8. [About the Author](#about-the-author)

## Description
This is a project to predict the price of a house based on the features of the house. The dataset used is the **USA_Housing** dataset which is available in the sklearn library. The dataset contains 50000 rows and 7 columns. The columns are as follows:

1. Avg. Area Income
2. Avg. Area House Age
3. Avg. Area Number of Rooms
4. Avg. Area Number of Bedrooms
5. Area Population
6. Price
7. Address


## Algorithm used
The algorithm used is the Linear Regression algorithm. The algorithm is implemented using the sklearn library. The accuracy of the model is 91.9%.

- Train technique used: train_test_split with 30% of the data as test data and random_state = 123
- Accuracy: 91.9%


## Server
The server is implemented using Django. The server is hosted on Render. The link to the server is: https://price-prediction-3l6g.onrender.com/

- The server is hosted on Render.com

## How to install and run the project
```bash
# clone the repository
git clone https://github.com/Adosh74/Property-Price-Prediction

# install the requirements
pip install -r requirements.txt

# run the server
python manage.py runserver
```
- **note:**
if you use linux comment line 28 in [views.py](/server/views.py) and uncomment line 25

## How to use the project
- Go to the link: https://price-prediction-3l6g.onrender.com/predict/
- Enter the values of the features
- Click on the predict button
- The predicted price will be displayed on the screen

## About the Model
- The model is trained using the Linear Regression algorithm with the sklearn library
- The model is trained on the Boston Housing dataset
- The model is trained with 70% of the data and tested with 30% of the data
- The accuracy of the model is 91.9%
- [Model Code](/model/Final-Model.ipynb)

# Screenshots
- **Home Page**
![Screenshot 1](/public/Home.jpg)
- **Predict Page**
![Screenshot 2](/public/Prediction_Page.jpg)
- **Result Page**
![Screenshot 3](/public/Result_Page.jpg)

## About the Author
- Name: **Mohamed Shebl**
- Collage: Faculty of Computer and Artificial Intelligence, Helwan University Software Engineering Department
- Blog: https://mohamedshebl.me
- Facebook: https://www.facebook.com/shebl74
- LinkedIn: https://www.linkedin.com/in/shebl74
- Email: mohamedshebla@gmail.com

