from flask import Flask, render_template, request, jsonify
from app import app  # Import the Flask app instance
from app.model import classify_message, generate_bot_response, load_data  # Import functions from the model module

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for processing user messages
@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    user_message = data['message']
    
    # Classify user message
    classification_result = classify_message(user_message)
    
    # Generate bot response
    bot_response = generate_bot_response(user_message)
    
    return jsonify({'classification_result': classification_result, 'bot_response': bot_response})

# Route for the chat page
@app.route('/chat')
def chat():
    # Load data from medicine_data.xlsx
    file_path = 'data/Medicine_description.xlsx'
    data = load_data(file_path)
    
    return render_template('chat.html', data=data)

# Route to handle POST requests for /get_bot_response
@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    # Get the message data from the request
    message = request.json.get('message')

    # Here you can add logic to process the message and generate bot response
    bot_response = generate_bot_response(message)

    # Return the response in JSON format
    return jsonify({'bot_response': bot_response})
