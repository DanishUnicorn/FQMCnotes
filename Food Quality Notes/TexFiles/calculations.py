# ----------------------------------------------- Case 5 calculations Cp calculations -----------------------------------------------

# Specification limits
USL = 16.3  # Upper Specification Limit (USL)
LSL = 15.7  # Lower Specification Limit (LSL)

# List of machine names
machine_names = ['Machine A', 'Machine B', 'Machine C', 'Machine D', 'Machine E']

# Std devs for the machines
std_devs = [0.05, 0.02, 0.10, 0.05, 0.20]  # Std devs for the 5 machines respectively

# Mean for the machines
means = [16.0, 16.2, 16.2, 15.9, 16.0]  # Means for the 5 machines respectively

# ----------------------------------------------- Case 5 calculations Cp calculations -----------------------------------------------

# Calculating Cp for each machine, using the formula Cp = (USL - LSL) / (6 * sigma)
Cp_values = [(USL - LSL) / (6 * sigma) for sigma in std_devs]

# Print the Cp values for each machine
for name, cp in zip(machine_names, Cp_values):
    print(f"{name} Cp value: {cp:.2f}")

# ----------------------------------------------- Case 5 calculations Cpk_u calculations -----------------------------------------------

# Calculating Cpk_u for each machine, using the formula Cpk_u = (USL - mean) / (3 * sigma)
Cpku_values = [(USL - mean) / (3 * sigma) for mean, sigma in zip(means, std_devs)]

# Print the Cpk_u values for each machine
for name, cp in zip(machine_names, Cpku_values):
    print(f"{name} Cpk_u value: {cp:.2f}")

# ----------------------------------------------- Case 5 calculations Cpk_l calculations -----------------------------------------------    

# Calculating Cpk_l for each machine, using the formula Cpk_l = (mean - LSL) / (3 * sigma)
CpkL_values = [(mean - LSL) / (3 * sigma) for mean, sigma in zip(means, std_devs)]

# Print the Cpk_l values for each machine
for name, cp in zip(machine_names, CpkL_values):
    print(f"{name} Cpk_l value: {cp:.2f}")