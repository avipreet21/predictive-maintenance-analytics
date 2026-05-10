import pandas as pd
import sklearn
print(sklearn.__version__)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

df = pd.read_csv("data/feature_engineered_predictive_maintenance.csv")

features = [col for col in df.columns if col not in ['Type','Machine failure', 'Tool wear failure', 'Heat dissipation failure', 'Power failure', 'Overstrain failure', 'Random failure']]

x = df[features]
y = df['Machine failure']

# Split the data into training and testing sets

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))