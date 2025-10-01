import tensorflow as tf
from tensorflow.keras import layers, models

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data to [0, 1] range
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build a simple neural network model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),         # Input layer
    layers.Dense(128, activation='relu'),         # Hidden layer
    layers.Dropout(0.2),                          # Dropout for regularization
    layers.Dense(10, activation='softmax')        # Output layer for 10 classes
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_split=0.1)

# Evaluate the model on test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')