# Importing necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

# Import data processing functions
from data_processing import process_data

def build_model(input_shape):
    """
    Function to build the machine learning model.
    This involves defining the architecture of the model, compiling the model, 
    and returning the model.
    """
    # Define the architecture of the model
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[input_shape]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    # Compile the model
    model.compile(loss='mean_squared_error',
                  optimizer=tf.keras.optimizers.RMSprop(0.001),
                  metrics=['mean_absolute_error', 'mean_squared_error'])

    return model

def train_model(model, features, labels, epochs):
    """
    Function to train the machine learning model.
    This involves fitting the model to the training data and returning the history of the training.
    """
    # Split the data into training and validation sets
    train_features, val_features, train_labels, val_labels = train_test_split(features, labels, test_size=0.2)

    # Fit the model to the training data
    history = model.fit(train_features, train_labels, epochs=epochs,
                        validation_data=(val_features, val_labels))

    return history

def evaluate_model(model, test_features, test_labels):
    """
    Function to evaluate the machine learning model.
    This involves evaluating the model on the test data and returning the results.
    """
    # Evaluate the model on the test data
    results = model.evaluate(test_features, test_labels, verbose=2)

    return results

def predict(model, new_data):
    """
    Function to make predictions using the machine learning model.
    This involves processing the new data, making predictions using the model, 
    and returning the predictions.
    """
    # Process the new data
    processed_data = process_data(new_data)

    # Make predictions using the model
    predictions = model.predict(processed_data)

    return predictions
