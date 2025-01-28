import matplotlib.pyplot as plt

# Provided data points
x_values = [0.9543839307760851, 0.8310305216485769, 0.6545379883410094,
            0.47426111415289807, 0.2407645978936519, 0.18749932901757438,
            0.14153166500263026, 0.06889915939321722, 0.060973514981695565]

y_values = [0.9603315189968543, 0.9530849088000687, 0.9415198557119391,
            0.9356071585773025, 0.8829430899545878, 0.8121463922616938,
            0.5871874563861423, 0.30985700022545015, 0.13304239535358098]
x_values=x_values[::-1]
x_values=y_values[::-1]
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')

plt.xlabel('X-values')
plt.ylabel('Y-values')
plt.title('Line Graph')
plt.grid(True)

plt.tight_layout()
plt.show()

