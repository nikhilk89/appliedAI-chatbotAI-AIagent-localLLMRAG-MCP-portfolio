#chatbot using gemini llm with memory saved in json file
import json
import os
from google import genai
from google.genai import types

#LLM API key
APIK = "LLM API KEY"
mem_file = "chat_history.json"

client = genai.Client(api_key=APIK)

#load memory function
def load_history():
    if os.path.exists(mem_file):
        with open(mem_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            #convert into gemini dict structure
            return [
                {"role": item["role"], "parts": [{"text": item["text"]}]}
                for item in data
            ]
    return []

#Save conversation function
def save_history(chat_session):
    save_data = []
    for msg in chat_session.get_history():
        # Safely extract text from the message parts
        if msg.parts:
            text = "".join(part.text for part in msg.parts if part.text)
        else:
            text = ""

        if text.strip():
            save_data.append({"role": msg.role, "text": text.strip()})

    with open(mem_file, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=2)

# open current chat session and load history
past_history = load_history()
chat_session = client.chats.create(
    model='gemini-2.5-flash',
    history=past_history  #Load mem file!
)


def chatg(ppt):
    response = chat_session.send_message(ppt)
    save_history(chat_session)  #save chat to mem file
    if response and response.text:
        return response.text.strip() #if blank prompt
    return ""


if __name__ == "__main__":
    print("Welcome to chatbot, ask a question'\n")
    while True:
        uin = input("you: ")
        if uin.lower() in ["exit", "quit"]:
            break
        response = chatg(uin)
        print("chatbot:", response, "\n")