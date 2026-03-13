# 🤖 Day 10 – Customer Buying Behavior AI Classifier

A Machine Learning project that trains an AI model to **predict whether a customer will buy a product** based on their behavior on a website.

This project demonstrates a **complete Machine Learning workflow** including dataset preparation, model training, prediction, evaluation, and visualization.

---

# 🎯 Project Objective

The goal of this project is to build an AI classifier that predicts:

**Will a customer buy a product or not?**

The model analyzes customer behavior and classifies them into two categories.

| Output | Meaning |
|------|------|
| 1 | Customer will buy the product |
| 0 | Customer will not buy the product |

---

# 📊 Dataset Information

The dataset contains **60 customer records**.

Each record includes the following features:

| Feature | Description |
|------|------|
| Age | Age of the customer |
| Minutes_on_Site | Time spent browsing the website |
| Bought_Product | Target variable (0 = No, 1 = Yes) |

Example dataset rows:

```
Age,Minutes_on_Site,Bought_Product
22,5,0
25,15,1
45,2,0
38,20,1
50,25,1
```

### Observed Pattern

Customers who spend **more time on the website** are more likely to **purchase the product**.

---

# 🧠 Machine Learning Workflow

This project follows a standard Machine Learning pipeline.

## 1️⃣ Load Dataset

```python
import pandas as pd
data = pd.read_csv("customer_data.csv")
```

---

## 2️⃣ Feature Selection

Input features:

```
Age
Minutes_on_Site
```

Target variable:

```
Bought_Product
```

---

## 3️⃣ Train-Test Split

The dataset is divided into training and testing data.

```
80% → Training Data
20% → Testing Data
```

Example:

```python
from sklearn.model_selection import train_test_split
```

---

## 4️⃣ Train the Model

A Logistic Regression classifier is used to train the AI model.

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
```

---

## 5️⃣ Predict Customer Behavior

The trained model predicts whether customers will buy a product.

```python
predictions = model.predict(X_test)
```

---

## 6️⃣ Model Evaluation

Model performance is evaluated using **Accuracy Score**.

```
Accuracy = Correct Predictions / Total Predictions
```

Example output from the terminal:

```
AI Classification Accuracy: 100.00%
The AI has successfully learned to predict human buying behavior.
```

---

# 📈 Data Visualization

A scatter plot was generated to visualize customer behavior.

Graph details:

- **X-axis:** Age  
- **Y-axis:** Minutes on Site  
- **Green points:** Customers who bought the product  
- **Red points:** Customers who did not buy  

The visualization clearly shows that customers who spend **more time on the website are more likely to purchase the product**.

---

# ⚙️ Technologies Used

Programming Language:

- Python

Libraries:

- Pandas
- Scikit-learn
- Matplotlib

Development Environment:

- VS Code

---

# 📂 Project Structure

```
AlphaDay10_ClassifierAI
│
├── classifier_ai.py
├── customer_data.csv
└── README.md
```

---

# 🚀 Key Learning

This project demonstrates a fundamental Machine Learning concept:

**AI models improve when they are trained on larger datasets.**

Initially the model used a very small dataset and achieved **low accuracy**.  
After upgrading to a larger dataset (60 records), the model successfully learned the pattern and achieved **100% classification accuracy**.

---

# 👩‍💻 Author

**Wajiha Arshad**

BS Data Science Graduate  
Python • Machine Learning • Data Analytics
