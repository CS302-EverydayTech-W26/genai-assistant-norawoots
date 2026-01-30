from gemini_client import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai-assistant', methods=['GET', 'POST'])
def ai_assistant():
    cur_client = GeminiClient()
    if request.method == 'POST':
        user_input = request.form.get('client_entry')
        try:
            response = cur_client.generate_response(user_input)
        except Exception as e:
            response = f"An error occurred: {e}"
        return render_template('ai-assistant.html', response=response, user_input=user_input)
    return render_template('ai-assistant.html', response=None, user_input=None)

def main():
    pass

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug = True)