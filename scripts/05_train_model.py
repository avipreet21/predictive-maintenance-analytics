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

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

confusion_df = pd.DataFrame(
    confusion_matrix(y_test, y_pred),
    index=["Actual Normal", "Actual Failed"],
    columns=["Predicted Normal", "Predicted Failed"]
)

print("\nFEATURE IMPORTANCE")
print(importance_df)
# Save model outputs to CSV files

importance_df.to_csv("Outputs/feature_importance.csv", index=False)
confusion_df.to_csv("Outputs/confusion_matrix.csv", index=False)

y_test.to_csv("Outputs/y_test.csv", index=False)
y_pred_df = pd.DataFrame(y_pred, columns=["Predicted Machine Failure"])
y_pred_df.to_csv("Outputs/y_pred.csv", index=False)