from gemini_client import *
import time

def main():
    cur_client = GeminiClient()
    user_input = ""
    print("Hello! I am your friendly GenAI assistant, and I am here to help!")
    time.sleep(2)
    print()
    print("When you are done, please type 'QUIT'. To get started, please enter a query...")
    time.sleep(1.5)
    print()
    while user_input != "QUIT":
        user_input = input("Ask anything: ")
        # user_input.capitalize()
        time.sleep(1)
        print()
        print("Processing...")
        cur_client.generate_response(user_input)
        print()
        

if __name__ == "__main__":
  main()