import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("--- Initializing AI Classifier ---")

# Step 1: Load Data
df = pd.read_csv("customer_data.csv")

# Step 2: Define Features and Target
X = df[['Age', 'Minutes_on_Site']]
y = df['Bought_Product']

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Predictions
predictions = model.predict(X_test)

# Step 6: Accuracy Score
score = accuracy_score(y_test, predictions)

print(f"AI Classification Accuracy: {score * 100:.2f}%")
print("The AI has successfully learned to predict human buying behavior.")
import matplotlib.pyplot as plt

# Plot customer data
plt.figure(figsize=(8,6))

for i in range(len(df)):
    if df['Bought_Product'][i] == 1:
        plt.scatter(df['Age'][i], df['Minutes_on_Site'][i], color='green', label='Bought' if i==1 else "")
    else:
        plt.scatter(df['Age'][i], df['Minutes_on_Site'][i], color='red', label='Not Bought' if i==0 else "")

plt.xlabel("Age")
plt.ylabel("Minutes on Site")
plt.title("Customer Buying Behavior Classification")
plt.legend()
plt.grid(True)

plt.show()