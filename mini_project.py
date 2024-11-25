import math
class MultiFunctionalChatbot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! I'm {self.name}. I can assist you with calculations and chat.")
        print("Type 'exit' to end the chat.")

    def respond(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input or "hi" in user_input:
            return "Hello! How are you today?"
        elif "how are you" in user_input:
            return "I'm just a program, but thanks for asking! How can I help you?"
        elif "what is your name" in user_input:
            return f"My name is {self.name}."
        elif "bye" in user_input or "exit" in user_input or "bie" in user_input:
            return "Goodbye! Have a great day!"
        else:
            return self.calculate(user_input)

    def calculate(self, user_input):
        try:
            user_input = user_input.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
            result = eval(user_input)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception:
            return "Invalid input. Please enter a valid input."

    def chat(self):
        self.greet()
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print(f"{self.name}: Goodbye! Have a great day!")
                break
            response = self.respond(user_input)
            print(f"{self.name}: {response}")

if __name__ == "__main__":
    bot = MultiFunctionalChatbot("ChatBot")
    bot.chat()
