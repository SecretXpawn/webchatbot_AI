from flask import render_template, request, jsonify
from app import app
from app.model import classify_message, generate_bot_response, load_data

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
    file_path = 'data/medicine_data.xlsx'
    data = load_data(file_path)
    
    return render_template('chat.html', data=data)
