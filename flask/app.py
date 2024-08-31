from flask import *
import asyncio
import ollama
# from ollama import AsyncClient,Client


app = Flask(__name__)


# async def chat():
#     message = [{
#         'role': 'system',
#         'content': 'You are a quiz generator. Generate quizzes with one question and four options. Mark the correct option.'
#     },
#     {
#         'role': 'user',
#         'content': '',
#     },]
    
#     response = await AsyncClient().chat(model='llama3.1:8b', messages=message)
#     print(response['message']['content'])


response = None
response = ollama.chat(model='llama3.1:8b', messages=[
   {
        'role': 'system',
        'content': 'You are a quiz generator. Generate quizzes with one question and four options. Mark the correct option.'
    },
  {
    'role': 'user',
    'content': 'article 92 of indian constitution',
  },
])

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return response['message']['content']
print('heledlfddfsdd')

# asyncio.run(chat())
# while True:
# print("D")