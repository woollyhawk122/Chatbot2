import datetime
from colorama import Fore, init
import random

init(autoreset=True)
user_input = "Hello"

def solve_math(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except (SyntaxError, NameError, ZeroDivisionError, TypeError):
        return None

def chatbot():
    print(Fore.GREEN + "ChatBot: HELLO! I'm your simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input(Fore.BLUE + "You: ").lower().strip()
        if user_input == "bye":
            print(Fore.GREEN + "ChatBot: Goodbye! Have a great day 😊")
            break
        elif "who made you" in user_input:
            print(Fore.GREEN + "ChatBot: I am made by Arjun")
        elif "can you do math" in user_input:
            print(Fore.GREEN + "ChatBot: Yes, I can do math")
        elif "your name" in user_input:
            print(Fore.GREEN + "ChatBot: I'm SimpleBot, your Python chatbot!")
        elif "what is valorant" in user_input:
            print(Fore.GREEN + "Chatbot:Valorant (stylized as VALORANT) is a 2020 first-person tactical hero shooter video game developed and published by Riot Games.[5] A free-to-play game, Valorant takes inspiration from the Counter-Strike series, borrowing several mechanics such as the buy menu, spray patterns, and inaccuracy while moving. Development started in 2014 and was teased under the codename Project A in 2019; the game was released on June 2, 2020, for Windows.")
        elif "what is war thunder" in user_input:
            print(Fore.GREEN + "Chatbot:War Thunder is a free-to-play online military combat game where players control real-world war vehicles like tanks, airplanes, helicopters, and warships in battles. It was developed by Gaijin Entertainment and first released in 2013.")
        elif "what is v ram" in user_input:
            print(Fore.GREEN + "Chatbot:V RAM stands for Video Random Access Memory. It is a special type of memory used by your graphics card (GPU) to store data needed to render images, videos, and games.")
        elif "what is the capital of france" in user_input:
            print(Fore.GREEN + "Chatbot: Capital of france is Paris ")
        elif "which company makes the playstation" in user_input:
            print(Fore.GREEN + "Chatbot: PlayStation is made by Sony")
        elif "what gas do humans breathe in to survive" in user_input:
            print(Fore.GREEN + "Chatbot: Humans breathe Oxygen to survive")
        elif "what is the fastest land animal" in user_input:
            print(Fore.GREEN + "Chatbot: Fastest land animal is Cheetah")
        elif "who was the first person to walk on the moon" in user_input:
            print(Fore.GREEN + "Chatbot: First person to walk on the Moon is Neil Armstrong")
        elif "what gas do plants absorb from the air" in user_input:
            print(Fore.GREEN + "Chatbot: Plants absorb Carbon dioxide from the air")
        elif "which company created the game fortnite?" in user_input:
            print(Fore.GREEN + "Chatbot: The company created Fortnite is Epic Games")
        elif "who is one of the most famous football players in the world" in user_input:
            print(Fore.GREEN + "Chatbot: One of the most famous football players in the world is Lionel Messi")
        elif "what company makes the iphone" in user_input:
            print(Fore.GREEN + "Chatbot: iPhone is made by Apple")
        elif "what is the closest star to earth" in user_input:
            print(Fore.GREEN + "Chatbot: The closest star to earth is the Sun")
        elif "who developed gta 5" in user_input:
            print(Fore.GREEN + "Chatbot: GTA 5 is developed by Rockstar Games")
        elif "who is adolf hitler" in user_input:
            print(Fore.GREEN + "Chatbot: Adolf Hitler (1889–1945) was a German dictator and leader of Nazi Germany.")
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(Fore.GREEN + f"ChatBot: The current time is {now}")
        elif "date" in user_input:
            today = datetime.date.today()
            print(Fore.GREEN + f"ChatBot: Today's date is {today}")
        elif user_input in ["hi", "hlo", "hello", "hey", "whats up"]:
            responses = [
                "Hello there!",
                "Hey!",
                "Nice to meet you!",
                "Hi! How can I help you?"
            ]
            print(Fore.GREEN + "ChatBot: " + random.choice(responses))
        elif "how are you" in user_input:
            print(Fore.GREEN + "ChatBot: I'm just a bot, but I'm doing great!")
        elif any(op in user_input for op in ["+", "-", "*", "/"]):
            answer = solve_math(user_input)
            if answer is not None:
                print(Fore.GREEN + f"ChatBot: The answer is {answer}")
            else:
                print(Fore.GREEN + "ChatBot: Sorry, I couldn't solve that.")
        else:
            default_responses = [
                "Interesting!",
                "Tell me more.",
                "I'm not sure I understand.",
                "Can you explain that?"
            ]
            print(Fore.GREEN + "ChatBot: " + random.choice(default_responses))

if __name__ == "__main__":
    chatbot()