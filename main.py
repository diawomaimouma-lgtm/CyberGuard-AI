from datetime import datetime
from chatbot import ChatBot
from colorama import Fore, Style, init

init(autoreset=True)  

def main():
    bot = ChatBot()

    print(f"{Fore.GREEN}=== Welcome to the Smart ChatBot! ===")
    print(f"{Fore.CYAN}commands: exit| clear | personality\n") 

    while True:
        user_input = input(f"{Fore.YELLOW}You: {Style.RESET_ALL}")

        if user_input.lower() in ["exit", "quit"]:
            print(f"{Fore.RED}Goodbye!")
            break
         
        elif user_input.lower() == "clear":
            bot.clear_history()
            continue
         
        elif user_input.lower().startswith("personality "):
            new_prompt = user_input.replace("personality", "").strip()
            bot.change_personality(new_prompt)
            continue
         
        response = bot.get_response(user_input)
        heure = datetime.now().strftime("%H:%M")
        print(f"{Fore.BLUE}[{heure}] {Fore.LIGHTBLUE_EX}Bot: {Style.RESET_ALL}{response}")


if __name__ == "__main__":
    main()  
 
