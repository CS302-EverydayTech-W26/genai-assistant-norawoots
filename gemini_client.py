from google import genai
import os
import sys
from google.genai import types, errors
import gemini_config as config
    
class GeminiClient:
    def __init__(self):
        gemini_api_key = config.GEMINI_API_KEY
        if gemini_api_key is None:
            print("Your API key is not set correctly!")
            sys.exit()
        else:
            self.client = genai.Client(api_key=gemini_api_key)
            self.chat_history = []

    def generate_response(self, user_input):
        try:
            if self.chat_history == None:  
                return "AI Assistant is not configured correctly"
            
            else:
                # TO DO: Modify system instruction based on the purpose of your GenAI Assistant
                my_system_instruction = "Be a helpful AI assistant. Thanks!"
                
                # Add the prompt to the chat history
                self.chat_history += [types.Content(
                    role='user',
                    parts=[types.Part.from_text(text=user_input)]
                    )]

                # TO DO: Use the client's chat history & system instruction to prompt Gemini
                response = self.client.models.generate_content(
                        model="gemini-3-flash-preview", 
                        config=types.GenerateContentConfig(system_instruction=my_system_instruction),
                        contents=self.chat_history
                    )
                
                # TO DO: Add the response text from Gemini to the client's chat history
                self.chat_history += [types.Content(
                    role='model',
                    parts=[types.Part.from_text(text=response.text)]
                    )]
                
                # TO DO: Return the response text from Gemini
                print(response.text)    
            return response.text

        except errors.ServerError as e:
            print("Sorry, I am experiencing a high request demand right now. Please try again later!")
            return "Sorry, I am experiencing a high request demand right now. Please try again later!"