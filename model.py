from google.genai import client
from dotenv import load_dotenv
import os
client = client.Client()
print(os.getcwd())

load_dotenv(override=True)
api_key = os.getenv('GOOGLE_API_KEY')


if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
else:
    print("API key found and looks good so far!")


shorter_system_prompt = """
Act as a story teller who teaches through real-life analogies.
first provide a shorter, simple English definition that can be understood in a single read.
Narrate the concepts using short, very simple, real lfe scnearios with the user as “you”.
Never Exceed the output more than 50 words. 
Respons as plain paragraph of sentences.
"""

user_prompt = """Here is the question user asking:"""


def prompt_generator(message):
    return f"{shorter_system_prompt}\n{user_prompt}\n{message}"


def mnemoniser(message):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt_generator(message)
    )
    return response.candidates[0].content.parts[0].text
