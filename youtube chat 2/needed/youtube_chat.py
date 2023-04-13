import pytchat
import openai
import pyttsx3
import keyboard
import time
import os
from gtts import gTTS

# Set up OpenAI API key
openai.api_key = "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"

# Set up GPT-3 language model
model_engine = "text-davinci-002"

# Set up text-to-speech engine
engine = pyttsx3.init()

def ytlivechat():
        chat = pytchat.create(video_id="uIx8l2xlYVY")
        while chat.is_alive():
           for c in chat.get().sync_items():
              print(f"[{c.author.name}]- {c.message}")
              
# Function to generate response using ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
def main():
    while True:
        chat = pytchat.create(video_id="_bKWrYbjz-Q") # Replace "4rmf-lk3ito" with the actual YouTube live video ID
        while chat.is_alive():
            for c in chat.get().sync_items():
                prompt = c.message
                response = generate_response(prompt)
                print(f"[{c.author.name}]- {prompt}")
                print("ChatGPT: " + response)               
                
if __name__ == '__main__':
    main()
          