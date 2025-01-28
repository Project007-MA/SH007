import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def plot1():
    # Method names
    methods = ['P-PNN', 'CNN', 'CNN-LSTM', 'RNN-LSTM']

    # Evaluation metrics
    accuracy = [98.684211, 95, 90.89, 95.78]
    precision = [98.930481, 94, 91.11, 95.81]
    recall = [99.462366, 95, 90.84, 95.78]
    f1 = [99.195710, 95, 90.89, 95.73]

    # Plotting
    x = range(len(methods))

    plt.figure(figsize=(10, 6))

    plt.bar(x, accuracy, width=0.2, label='Accuracy')
    plt.bar([i + 0.2 for i in x], precision, width=0.2, label='Precision')
    plt.bar([i + 0.4 for i in x], recall, width=0.2, label='Recall')
    plt.bar([i + 0.6 for i in x], f1, width=0.2, label='F1')

    plt.xlabel('Methods')
    plt.ylabel('Percentage')

    plt.xticks([i + 0.3 for i in x], methods)
    plt.legend()

    plt.tight_layout()
    plt.savefig("Results/figure3.png",dpi=800)
    plt.show()

def plot2():


    # Creating a dataframe for the data
    data = {
        'Method': ['ECC', 'AES', 'FK-ECC', 'ECC', 'AES', 'FK-ECC'],
        'Time Type': ['Encryption', 'Encryption', 'Encryption', 'Decryption', 'Decryption', 'Decryption'],
        'Time (s)': [0.22, 0.634, 0.19, 0.14, 0.34, 0.12]
    }
    df = pd.DataFrame(data)

    # Plotting the bar plot using seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Method', y='Time (s)', hue='Time Type', data=df)

    # Adding labels and title
    plt.xlabel('Encryption Methods', fontweight='bold')
    plt.ylabel('Time (s)', fontweight='bold')


    # Save the plot to a file
    plt.savefig('Results/figure',dpi=400)
    plt.show()


#plot1()
plot2()

import matplotlib.pyplot as plt
import numpy as np

# Data
methods = ['AI', 'Median', 'Gaussian', 'PSD-AI']
psnr_values = [3, 17.4, 28.7, 39.605]
ssim_values = [0.7015, 0.7089, 0.9052, 0.96]

# Define the width of the bars
bar_width = 0.35

# Create positions for the bars
r1 = np.arange(len(methods))
r2 = [x + bar_width for x in r1]

# Create the figure and the axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting PSNR values
bars1 = ax1.bar(r1, psnr_values, color='b', width=bar_width, edgecolor='grey', label='PSNR')
ax1.set_xlabel('Methods', fontweight='bold')
ax1.set_ylabel('PSNR (dB)', color='b', fontweight='bold')
ax1.set_xticks([r + bar_width/2 for r in range(len(methods))])
ax1.set_xticklabels(methods)
ax1.tick_params(axis='y', labelcolor='b')

# Adding a second y-axis for SSIM values
ax2 = ax1.twinx()
bars2 = ax2.bar(r2, ssim_values, color='r', width=bar_width, edgecolor='grey', label='SSIM')
ax2.set_ylabel('SSIM', color='r', fontweight='bold')
ax2.tick_params(axis='y', labelcolor='r')



# Add a legend
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))

# Show plot
plt.tight_layout()
plt.savefig("Results/figure5.png",dpi=800)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data
methods = ['AI', 'Median', 'Gaussian','PSD-AI']
values = [2388.6,1854.4,1995.3,1389.9]

# Create the bar plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plotting PSNR values
bars = ax.bar(methods, psnr_values, color='blue', edgecolor='grey')

# Add labels and title
ax.set_xlabel('Methods', fontweight='bold')
ax.set_ylabel('time(ms)', fontweight='bold')

ax.bar(methods, values, color='lightgreen', edgecolor='grey')


# Show plot
plt.tight_layout() 
plt.savefig("Results/figure6.png",dpi=800)
plt.show()


