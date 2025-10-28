import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# Set up the Flask app
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable Cross-Origin Resource Sharing

# --- 1. Load API Key ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# --- 2. Load "Training" Context ---
try:
    with open('context.txt', 'r') as f:
        my_context = f.read()
except FileNotFoundError:
    print("Warning: context.txt not found. AI will not have personal info.")
    my_context = "Lemi is a software developer. [CONTEXT FILE IS MISSING]"

# --- 3. Set up the System Prompt ---
SYSTEM_PROMPT = f"""
You are a professional, helpful, and friendly AI assistant for Lemi, a software developer.
Your job is to answer questions from potential employers who visit his portfolio website.
Base your answers *only* on the context provided below. Do not make things up.
If the answer is not in the context, politely say "I do not have that information, but Lemi would be happy to discuss it with you."

--- BEGIN CONTEXT ---
{my_context}
--- END CONTEXT ---
"""

# --- 4. Create the Web Endpoints ---
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if not GEMINI_API_KEY:
        return jsonify({'error': 'Server is not configured with an API key.'}), 500

    try:
        user_message = request.json['message']

        # FIXED: Use the correct model name (without version suffix)
        model = genai.GenerativeModel('models/gemini-2.5-flash')
        chat_session = model.start_chat(
            history=[
                {'role': 'user', 'parts': [SYSTEM_PROMPT]},
                {'role': 'model', 'parts': ["Understood. I am Lemi's AI assistant. I will answer questions based only on the provided context."]}
            ]
        )
        
        response = chat_session.send_message(user_message)
        
        return jsonify({'reply': response.text})

    except Exception as e:
        error_message = str(e)
        print(f"An error occurred: {error_message}")
        return jsonify({'error': f'An internal server error occurred: {error_message}'}), 500

if __name__ == '__main__':
    # Using port 5003
    app.run(host='0.0.0.0', port=5001, debug=True)