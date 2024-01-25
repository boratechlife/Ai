import tensorflow as tf

# Load the model (make sure the path is correct and accessible)
model = tf.keras.models.load_model('./my_model.h5')

def preprocess_input(text):
    return processed_text

def make_prediction():
    user_input = Element('user-input').element.value  # Get the user input
    processed_input = preprocess_input(user_input)    # Preprocess the input
    
    # Make a prediction
    prediction = model.predict(processed_input)
    
    # Assuming your model outputs probabilities for each class
    predicted_class_index = prediction.argmax()  # Get the index of the highest probability
    
    # Convert the predicted class index to the actual category name
    predicted_category = category_mapping[predicted_class_index]
    
    # Display the result
    Element('prediction-result').element.innerHTML = predicted_category

# Expose the make_prediction function to the global scope
window.makePrediction = make_prediction