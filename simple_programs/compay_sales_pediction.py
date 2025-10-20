import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import io
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Download dataset from URL
url = "https://gist.githubusercontent.com/vivek2606/f2e92da495b3cc06982b6f656bda5005/raw/advertising.csv"
# (This URL is from the GitHub gist version) :contentReference[oaicite:3]{index=3}

response = requests.get(url)
response.raise_for_status()  # will stop if there's an error
data = pd.read_csv(io.StringIO(response.text))

print("Dataset head:")
print(data.head())

# Step 2: Basic EDA
print("\nMissing values:\n", data.isnull().sum())
sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.show()

# Step 3: Define features & target
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Step 4: Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train model (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict & evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nModel Performance:")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Step 7: Visualize actual vs predicted
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()

# Step 8: Feature coefficients
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print("\nFeature Coefficients:\n", coefficients)
