import openai
import os
from dotenv import load_dotenv
import sqlite3
import uuid

load_dotenv()

openai.api_key = os.getenv("OPEN_API_NEW_KEY")

def get_response_from_chat_gpt(text):
    print("getting a response from chat gpt for the text", text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are world class psychologist who are incredibly compassionate and understanding. You give everyone excellent advice on how to improve their life."},
            {"role": "user", "content": text}
        ]
    )

    text = response['choices'][0]['message']['content']
    return text


# Connect to SQLite database
conn = sqlite3.connect('chats.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS chats
             (id TEXT, text TEXT, response TEXT)''')


def get_response_from_chat_gpt_psychology(prompt, uuid):
    print("getting a response from chat gpt for the text", prompt)

    # Retrieve previous messages from the database
    c.execute("SELECT text, response FROM chats WHERE id = ?", (uuid,))
    rows = c.fetchall()

    # Format previous messages for inclusion in the chat
    previous_messages = []
    for row in rows:
        # print("the previous message from user is", row[0])
        # print("the previous message from assistant is", row[1])
        previous_messages.append({"role": "user", "content": row[0]})
        previous_messages.append({"role": "assistant", "content": row[1]})

    # Include system message, previous messages, and the new user message in the messages list
    messages = [
        {"role": "system", "content": """
                You are a psychologist and use your language to help patients with their problems.
                """}
    ] + previous_messages + [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    text_response = response['choices'][0]['message']['content']

    # Store text and response in the database
    c.execute("INSERT INTO chats VALUES (?,?,?)", (uuid, prompt, text_response))
    conn.commit()

    return text_response

def create_unit_test(text):
    print("getting a response from chat gpt for the text", text)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Write the worlds greatest unit test for the following code. Only respond with code, no text"},
            {"role": "user", "content": text}
        ]
    )

    text = response['choices'][0]['message']['content']

    return text



# print(get_response_from_chat_gpt("I am feeling anxious."))