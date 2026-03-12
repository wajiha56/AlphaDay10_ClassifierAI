# 🤖 Day 10 – AI Classifier (Customer Buying Prediction)

## 📌 Project Overview

This project demonstrates how to build a **Machine Learning Classification Model** using **Logistic Regression** in Python.

Unlike regression models that predict **numbers**, this AI model predicts **categories**. In this case, it predicts whether a **customer will buy a product or not** based on their behavior.

The AI analyzes customer characteristics such as **Age** and **Time Spent on Website** to classify purchasing behavior.

---

# 🎯 Project Objective

The goal of this project is to:

* Train an AI model to **predict customer decisions**
* Implement **Logistic Regression for classification**
* Evaluate model performance using **Accuracy Score**
* Simulate a **real-world marketing prediction system**

---

# 🧠 Machine Learning Concept Used

## Classification

Classification is a type of machine learning used to predict **categories or labels** instead of numbers.

Examples of classification problems:

| Problem                      | Output               |
| ---------------------------- | -------------------- |
| Email Spam Detection         | Spam / Not Spam      |
| Medical Diagnosis            | Disease / No Disease |
| Customer Purchase Prediction | Buy / Not Buy        |
| Fraud Detection              | Fraud / Safe         |

In this project, the AI predicts:

```
1 = Customer bought the product
0 = Customer did not buy the product
```

---

# ⚙️ Machine Learning Algorithm Used

### Logistic Regression

Logistic Regression is one of the most common algorithms used for **binary classification problems**.

It calculates the probability that a certain event will occur.

Example:

```
Probability of Buying = 0.82
```

If probability > 0.5 → **Customer buys product**

---

# 📂 Project Structure

```
AlphaDay10_ClassifierAI
│
├── classifier_ai.py       # Machine Learning classification script
├── customer_data.csv      # Sample customer dataset
└── README.md              # Project documentation
```

---

# 📊 Dataset Description

The dataset contains simple customer behavior information.

| Column          | Description                         |
| --------------- | ----------------------------------- |
| Age             | Customer age                        |
| Minutes_on_Site | Time spent on website               |
| Bought_Product  | Purchase decision (1 = Yes, 0 = No) |

Example dataset:

```
Age,Minutes_on_Site,Bought_Product
22,5,0
25,15,1
45,2,0
38,20,1
```

---

# ⚙️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Machine Learning (Classification)

---

# 🚀 How to Run the Project

### Step 1 — Install Required Libraries

```
pip install pandas scikit-learn
```

---

### Step 2 — Navigate to the Project Folder

```
cd AlphaDay10_ClassifierAI
```

---

### Step 3 — Run the Python Script

```
python classifier_ai.py
```

---

# 💻 Expected Output

```
--- Initializing AI Classifier ---
AI Classification Accuracy: 50.00%
The AI has successfully learned to predict human buying behavior.
```

Accuracy may vary depending on the training and test data.

---

# 📈 Business Value

This type of AI system can help businesses:

* Predict **which customers are likely to buy**
* Improve **marketing targeting**
* Increase **sales conversion rates**
* Personalize customer experiences

---

# 🌍 Real-World Applications

Classification models are widely used in:

* Email spam filters
* Credit card fraud detection
* Customer churn prediction
* Medical diagnosis systems
* Recommendation engines

---

# 👩‍💻 Author

**Wajiha Arshad**
BS Data Science Graduate | Machine Learning Enthusiast

Skills Demonstrated:

* Machine Learning Classification
* Logistic Regression
* Data Analysis
* Python Programming

---

# ⭐ Project Summary

This project demonstrates how machine learning can analyze **customer behavior data** and classify purchasing decisions.

By implementing **Logistic Regression and Accuracy Evaluation**, this AI model simulates a real-world **customer behavior prediction system** used in modern marketing analytics.

---
