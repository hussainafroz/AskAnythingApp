from flask import Flask, render_template, request, jsonify
import gpt_turbo
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    #return get_Chat_response(input)
    #return llb_chat_response(input)
    return gpt3_chat_response(input)

def gpt3_chat_response(text):
   return gpt_turbo.get_response(text)
if __name__ == '__main__':
    app.run()
