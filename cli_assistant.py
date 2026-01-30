from gemini_client import *
import time

def main():
    cur_client = GeminiClient()
    user_input = ""
    print("Hello! I am your friendly GenAI assistant, and I am here to help!")
    time.sleep(2)
    print()
    print("When you are done, please type 'exit'. To get started, please enter a query...")
    time.sleep(1.5)
    print()
    user_input = input("Ask anything: ")
    while user_input != "exit":
        time.sleep(1)
        print()
        print("Processing...")
        cur_client.generate_response(user_input)
        print()
        user_input = input("Ask anything: ")
    print()
    print("Goodbye!")
    
        

if __name__ == "__main__":
  main()