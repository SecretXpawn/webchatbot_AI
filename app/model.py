import openai
import pandas as pd
import tensorflow as tf
import requests
def load_data(file_path):
    data = pd.read_excel(file_path)
    return data

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(100,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

def classify_message(message):
    model = create_model()
    prediction = model.predict(message)
    return prediction
def generate_bot_response(message):
    try:
        api_key = 's'
        openai.api_key = api_key
    
        response = openai.Completion.create(
            engine="davinci-002",  
            prompt=prompt,         
            max_tokens=100,        
            temperature=0.7,       
            stop=["\n"]            
        )
        bot_response = response.choices[0].text.strip()

        return bot_response
    except Exception as e:
        # Handle any exceptions that may occur during API call
        print("Error:", e)
        return "Sorry, I couldn't generate a response at the moment."

prompt = "your name is Dr. Dika is a doctor specializing in elderly people and speak indonesian, lern medicine in data Patch exel i gave you. Write and run code to answer questions."

bot_response = generate_bot_response(prompt)
print(bot_response)  
