import pandas as pd
import numpy as np

df = pd.read_csv("data/cleaned_predictive_maintenance.csv")

# Create a new feature: "Power"

df['power'] = (df['torque_nm'] * df['rotational_speed_rpm']) / 9550

# Create a new feature: "Temperature difference"

df['temperature difference'] = df['process_temperature_k'] - df['air_temperature_k']

# Create a new feature: "high temperature flag"
df['high_temperature_flag'] = (df['process_temperature_k'] > df['process_temperature_k'].quantile(0.9)).astype(int)

# Create a new feature: "high torque flag"
df['high_torque_flag'] = (df['torque_nm'] > df['torque_nm'].quantile(0.9)).astype(int)

# Create a new feature: "low rotational speed flag"
df['low_rotational_speed_flag'] = (df['rotational_speed_rpm'] < df['rotational_speed_rpm'].quantile(0.1)).astype(int)
 
# Wear stress feature
df["wear_Stress"] = (
    df["tool_wear_min"] *
    df["torque_nm"]
)
print(df.head())
print(df.columns)
df.to_csv("data/feature_engineered_predictive_maintenance.csv", index=False)