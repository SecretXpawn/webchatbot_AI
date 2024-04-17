from flask import Flask, render_template, request, jsonify
from app import app 
from app.model import classify_message, generate_bot_response, load_data  
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    user_message = data['message']
    
    classification_result = classify_message(user_message)
 
    bot_response = generate_bot_response(user_message)
    
    return jsonify({'classification_result': classification_result, 'bot_response': bot_response})

@app.route('/chat')
def chat():

    file_path = 'data/Medicine_description.xlsx'
    data = load_data(file_path)
    
    return render_template('chat.html', data=data)

@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    message = request.json.get('message')

    bot_response = generate_bot_response(message)

    return jsonify({'bot_response': bot_response})
