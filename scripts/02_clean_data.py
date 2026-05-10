import pandas as pd

df = pd.read_csv("data/ai4i2020.csv")

df =df.drop(columns=['UDI', 'Product ID'])

df =df.rename(columns={'Air temperature [K]': 'air_temperature_k','Process temperature [K]': 'process_temperature_k', 'Rotational speed [rpm]': 'rotational_speed_rpm', 'Torque [Nm]': 'torque_nm', 'Tool wear [min]': 'tool_wear_min','TWF': 'Tool wear failure', 'HDF': 'Heat dissipation failure', 'PWF': 'Power failure', 'OSF': 'Overstrain failure', 'RNF': 'Random failure'}, inplace=False)


print("Cleaned dataset:")
print(df.head())

# Save cleaned dataset
df.to_csv("data/cleaned_predictive_maintenance.csv", index=False)