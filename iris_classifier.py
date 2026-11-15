
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a machine learning model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Iris Flower Classification")
print("--------------------------")
print(f"Model Accuracy: {accuracy:.2%}")

# Test a sample prediction
sample = [[5.1, 3.5, 1.4, 0.2]]
result = model.predict(sample)

print("Predicted Flower:", iris.target_names[result[0]])
