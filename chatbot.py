import groq
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# charger les variables du fichier .env
load_dotenv()

# recuperer la clé API depuis l'environnement
api_key = os.getenv("groq_api_key")

if not api_key:
    raise ValueError("Erreur : GROQ_API_KEY est introuvable. verifier votre fichier .env")

client = groq.Groq(api_key=api_key)


class ChatBot:
    def __init__(self, model="llama-3.3-70b-versatile", max_history=10):
        self.model = model
        self.max_history = max_history
        self.history = []
        self.system_prompt = "You are a highly serious cybersecurity expert."
        self.load_history()

    def add_to_history(self, role, message):
        self.history.append({
            "role": role,
            "content": message, 
            "time": datetime.now().strftime("%H:%M:%S")

        })

        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]

    def get_response(self, user_input):
        self.add_to_history("user", user_input)
        
        try: 
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": self.system_prompt}] + 
                         [{"role": m["role"], "content": m["content"]} for m in self.history],
                max_tokens=200,
                temperature=0.7

            )
             
            answer = response.choices[0].message.content
            self.add_to_history("assistant", answer)
            self.save_history()

            return answer
        
        except Exception as e:
            return f"Erreur API: {str(e)}"

    def save_history(self):
        data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "model": self.model,
            "messages": self.history
        }
        try:
            with open("chat_history.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving history: {e}")

    def load_history(self):
        try:
            with open("chat_history.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.history = data.get("messages", [])
                print("historique chargé.")
        except (FileNotFoundError, json.JSONDecodeError):
            self.history = []
            print("Aucun historique trouvé, démarrage avec un historique vide.")    

    def clear_history(self):
        self.history = []
        print("historique supprimé.") 

    def change_personality(self, new_prompt):
        self.system_prompt = new_prompt
        print(f"Personality changed to: {new_prompt}")
