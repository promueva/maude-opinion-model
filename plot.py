import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Load the CSV file
#file_path = "./results/results-metadata.csv"
#file_path = "./results/results-uniform.csv"
file_path = "./results/results-comp.csv"
# Reload the CSV using the correct delimiter
df = pd.read_csv(file_path, delimiter=';')

# Create the smoothed plot without dots
plt.figure(figsize=(10, 6))

for agent, group in df.groupby('agents'):
    group_sorted = group.sort_values('comms')
    x = group_sorted['comms'].values
    y = group_sorted['mean'].values

    # Interpolate for smooth curves
    if len(x) >= 4:
        x_new = np.linspace(x.min(), x.max(), 300)
        spline = make_interp_spline(x, y, k=3)
        y_smooth = spline(x_new)
        plt.plot(x_new, y_smooth, label=f'Agent {agent}')
    else:
        plt.plot(x, y, label=f'Agent {agent}')

plt.xlabel('Number of Communications')
plt.ylabel('Expected Probability')
#plt.title('Smoothed Mean vs Comms for Each Agent (No Markers)')
plt.legend(title='Number of Agents')
plt.xlim(0, 400)
plt.grid(True)
plt.tight_layout()
#plt.show()
#plt.savefig("metadata.png")
#plt.savefig("uniform.png")
plt.savefig("compare.png")
