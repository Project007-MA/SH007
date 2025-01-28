import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Example data (replace this with your actual data)
# Assuming `t_frame` is your feature data and `label` is your target data
# Also assuming `t_frame` is an array of image data of shape (num_samples, height, width, num_channels)

# Replace with your actual data loading code
t_frame = np.random.rand(1000, 28, 28, 1)  # Example: 1000 grayscale images of 28x28 pixels
label = np.random.randint(0, 10, 1000)  # Example: 1000 labels for 10 classes

# One-hot encode the labels if they are not already
y = to_categorical(label, num_classes=10)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(t_frame, y, test_size=0.3, random_state=42)

# Define the CNN model
model = Sequential()

# Add convolutional layers
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten the output from the convolutional layers
model.add(Flatten())

# Add dense layers
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))  # Dropout for regularization
model.add(Dense(10, activation='softmax'))  # Output layer for 10 classes

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model on the test data
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_accuracy:.4f}')
