import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load outputs from model
df_importance = pd.read_csv("Outputs/feature_importance.csv")
df_confusion = pd.read_csv("Outputs/confusion_matrix.csv", index_col=0)


plt.figure(figsize=(10,6))
plt.bar(df_importance["Feature"], df_importance["Importance"])
plt.title("Feature Importance from Random Forest Model")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("Charts/model_feature_importance_bar.png")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df_confusion, annot = True, fmt = "d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.savefig("Charts/model_confusion_matrix.png")
plt.show()