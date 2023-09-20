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
            {"role": "system", "content": """You are a super smart developer using Test Driven Development to write tests according to a specification. Please generate tests based on the above specification. The tests should be as simple as possible, but still cover all the functionality. Comments should be included in the tests to explain what they are testing in python comment notation."""},
            {"role": "user", "content": text}
        ]
    )

    text = response['choices'][0]['message']['content']

    return text


def code_review(text):
    #print("getting a response from chat gpt for code review for the text", text)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a the worlds greatest developer assigned to review the code below. Review with empathy and clarity, prioritize architecture and maintainability, understand context, ensure functionality, and provide constructive feedback."},
            {"role": "user", "content": text}
        ]
    )

    text = response['choices'][0]['message']['content']
    #print("the response for code review is", text)

    return text

def get_youtube_link_from_response(text):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Based on the following text, what would be a good search string to use on youtube to find a video that gives more information about the topics in the text?"},
        {"role": "user", "content": text + "Your response should ONLY BE THE SEARCH STRING."}
        ]
    )

    text_response = response['choices'][0]['message']['content']
    return text_response



# print(get_response_from_chat_gpt("I am feeling anxious."))