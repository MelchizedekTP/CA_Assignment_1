import csv
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler # this is used to get values between 0 and 1 for the scaled values in X

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
# Input file from previous step
input_file = input("Enter the file having the processed data")
input_file=input_file + ".csv"
X = []
Y = []

# Read processed_data.csv
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        if not row:
            continue
        # row[0] is X in string form like "[113158,163982,...]"
        x_str = row[0].strip("[]")
        x_vals = [float(v) for v in x_str.split(",")]
        X.append(x_vals)
        Y.append(float(row[1]))

X = np.array(X)
Y = np.array(Y)


# Normalize X using standard normal distribution (z-score)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, Y, test_size=0.3, random_state=23)

# Train Linear Regression model
model = LinearRegression(positive=True)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

n = X_test.shape[0]  # number of observations
p = X_test.shape[1]  # number of parameters in X
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

# Metrics
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", rmse)
print("R² Score:", r2)
print("adj_r2:", adj_r2)


residuals = y_test - y_pred
print("\nResiduals:", residuals)


X_train_sm = sm.add_constant(X_train)
ols_model = sm.OLS(y_train, X_train_sm).fit()

print("\n--- Statsmodels Summary ---")
print(ols_model.summary())











