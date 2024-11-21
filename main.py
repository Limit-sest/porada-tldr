from library import bakalari, discord, utils
from dotenv import dotenv_values
import os.path
import google.generativeai as genai


class Meeting:
    def __init__(self, date: str, meeting_content: str, chat_history: list):
        self.date = date
        self.meeting_content = meeting_content
        self.chat_history = chat_history


if not os.path.exists('.env'):
    utils.setup()
secrets = dotenv_values('.env')

# Gemini code
genai.configure(api_key=secrets['GEMINI_API_KEY'])

