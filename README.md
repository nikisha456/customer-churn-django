# Customer Churn Prediction Web Application

## Project Overview

This is a Machine Learning + Django web application that predicts whether a customer will **churn (leave)** or **stay** based on their details.

The model is trained using a dataset containing customer information like age, purchase history, and account details.

---

## Dataset Information

The dataset includes the following columns:

* Age
* Total_Purchase
* Account_Manager (0 or 1)
* Years
* Num_Sites
* Churn (Target Variable)

 Target:

* **1 = Customer will churn**
* **0 = Customer will stay**

---

## Technologies Used

* Python
* Django
* Scikit-learn
* Pandas
* HTML

---

## Machine Learning Model

* Model Used: Random Forest Classifier
* Trained using Scikit-learn
* Saved using Joblib

---

## Web Application Features

* User input form
* Real-time prediction
* Simple UI
* Backend ML integration

---

## How to Run the Project

1. Clone the repository:

   ```
   git clone https://github.com/nikisha456/customer-churn-django.git
   ```

2. Navigate to project folder:

   ```
   cd DS_Django_Project
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Train the model:

   ```
   python train_model.py
   ```

5. Run Django server:

   ```
   cd webapp
   python manage.py runserver
   ```

6. Open browser:

   ```
   http://127.0.0.1:8000/
   ```

---

## Project Outcome

This project demonstrates:

* End-to-end data science workflow
* Model deployment using Django
* Integration of ML with web applications

---

## Author

Nikisha Gupta
