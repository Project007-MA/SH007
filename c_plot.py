import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'

# Data preparation
data = {
    'Model': ['CNN', 'LSTM', 'RNN-LSTM', 'Proposed P-PNN'],
    'Accuracy (%)': [77.64, 95.71, 95.78, 98.68],
    'Precision (%)': [75.35, 96, 95.81, 98.93],
    'Recall (%)': [84.70, 95.71, 95.78, 99.46]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format for Seaborn
df_melted = df.melt('Model', var_name='Metric', value_name='Value')

# Define markers and dashes for each metric
markers = ['o', 's', 'D']  # Circle for Accuracy, Square for Precision, Diamond for Recall
dashes = {
    'Accuracy (%)': '',     # Solid line
    'Precision (%)': (2, 2), # Dashed line
    'Recall (%)': (5, 2)    # Dotted line
}

# Plotting
plt.figure(figsize=(10, 6))
sns.lineplot(
    data=df_melted,
    x='Model',
    y='Value',
    hue='Metric',
    style='Metric',
    markers=markers,
    markersize=10,
    dashes=dashes
)


plt.xlabel('Metrices',fontsize=16,fontweight='bold')
plt.ylabel('Values',fontsize=16,fontweight='bold')
plt.legend(title='Metric')
plt.grid(True)
plt.xticks(fontsize=14,fontweight='bold')
plt.yticks(fontsize=14,fontweight='bold')
# Show plot
plt.tight_layout()
plt.savefig("c_plot1",dpi=400)
plt.show()
