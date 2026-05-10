import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_predictive_maintenance.csv")

Total_failures = df['Machine failure'].sum()
OverStrain_failures = df['Overstrain failure'].sum()
Tool_wear_failures = df['Tool wear failure'].sum()
Heat_dissipation_failures = df['Heat dissipation failure'].sum()
Power_failures = df['Power failure'].sum()
Random_failures = df['Random failure'].sum()

failure_modes = ['OverStrain', 'Tool Wear', 'Heat Dissipation', 'Power', 'Random']
failure_mode_counts = [ OverStrain_failures, Tool_wear_failures, Heat_dissipation_failures, Power_failures, Random_failures]

# Plotting the failure mode counts
plt.figure(figsize=(10,6))
plt.bar(failure_modes, failure_mode_counts)
plt.title("Failure Mode Counts")
plt.xlabel("Failure Modes")
plt.ylabel("Count of Failures")
plt.savefig("charts/failure_mode_counts_bar.png")
plt.show()

# Plotting the distribution of machine failures
plt.figure(figsize=(8,8))
plt.pie(
    failure_mode_counts,
    labels=failure_modes,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Failure Mode Percentage Distribution")
plt.savefig("charts/failure_mode_distribution_pie.png")
plt.show()

# Plotting process temperature vs rotor speed colored by machine failure

normal = df[df["Machine failure"] == 0]
failed = df[df["Machine failure"] == 1]

plt.figure(figsize=(10,6))
plt.scatter(normal['process_temperature_k'], normal['rotational_speed_rpm'], alpha=0.3, label='Normal')
plt.scatter(failed['process_temperature_k'], failed['rotational_speed_rpm'],  alpha=0.9, label='Failed')
plt.title("Process Temperature vs Rotor Speed Colored by Machine Failure")
plt.xlabel("Process Temperature [K]")
plt.ylabel("Rotational Speed [rpm]")
plt.colorbar(label='Machine Failure')
plt.savefig("charts/temperature_vs_rotor_speed.png")
plt.show()

# Plotting torque vs rotor speed colored by machine failure
plt.figure(figsize=(10,6))
plt.scatter(normal["torque_nm"], normal['rotational_speed_rpm'], alpha=0.3, label='Normal')
plt.scatter(failed["torque_nm"], failed['rotational_speed_rpm'], alpha=0.9, label='Failed')
plt.title("Torque vs Rotor Speed Colored by Machine Failure")
plt.xlabel("Torque [Nm]")
plt.ylabel("Rotor Speed [rpm]")
plt.colorbar(label='Machine Failure')
plt.savefig("charts/torque_vs_rotor_speed.png")
plt.show()

normal = df[df["Heat dissipation failure"] == 0]
failed = df[df["Heat dissipation failure"] == 1]
# Plotting process temperature vs rotor speed colored by Heat dissipation failure

plt.figure(figsize=(10,6))
plt.scatter(normal['process_temperature_k'], normal['rotational_speed_rpm'],  alpha=0.3, label='Normal')
plt.scatter(failed['process_temperature_k'], failed['rotational_speed_rpm'],  alpha=0.9, label='Failed')
plt.title("Process Temperature vs Rotor Speed Colored by Heat Dissipation Failure")
plt.xlabel("Process Temperature [K]")
plt.ylabel("Rotational Speed [rpm]")
plt.colorbar(label='Heat Dissipation Failure')
plt.savefig("charts/temperature_vs_rotor_speed_heat_dissipation.png")
plt.show()


normal = df[df["Overstrain failure"] == 0]
failed = df[df["Overstrain failure"] == 1]

# Plotting torque vs rotor speed colored by overstrain failure
plt.figure(figsize=(10,6))
plt.scatter(normal["torque_nm"], normal['rotational_speed_rpm'], alpha=0.3, label='Normal')
plt.scatter(failed["torque_nm"], failed['rotational_speed_rpm'], alpha=0.9, label='Failed')
plt.title("Torque vs Rotor Speed Colored by Overstrain Failure")
plt.xlabel("Torque [Nm]")
plt.ylabel("Rotor Speed [rpm]")
plt.colorbar(label='Overstrain Failure')
plt.savefig("charts/torque_vs_rotor_speed_overstrain.png")
plt.show()

# Plotting torque vs rotor speed colored by power failure
normal = df[df["Power failure"] == 0]
failed = df[df["Power failure"] == 1]

plt.figure(figsize=(10,6))
plt.scatter(normal["torque_nm"], normal['rotational_speed_rpm'], alpha=0.3, label='Normal')
plt.scatter(failed["torque_nm"], failed['rotational_speed_rpm'], alpha=0.9, label='Failed')
plt.title("Torque vs Rotor Speed Colored by Power Failure")
plt.xlabel("Torque [Nm]")
plt.ylabel("Rotor Speed [rpm]")
plt.colorbar(label='Power Failure')
plt.savefig("charts/torque_vs_rotor_speed_power.png")
plt.show()