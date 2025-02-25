from flask import Flask, render_template, request
from groq import Groq
import os

app = Flask(__name__)

def generate_response(field, weather, history, soil, query):
    field = input("What stage is your field in? ")
    weather = input("How have recent weather conditions been? ")
    history = input("Have your crops experienced anything in the past? ")
    soil = input("What soil type do you have? ")
    user_query= input("Ask a question about farming! ")
    
    
    prompt = f"""
    You are a farming assistant who is going to help farmers answer questions about diseases or help them identify actionable solutions to any other farming related problems that they may be facing.

    Always answer with step by step actionable solutions that the farmer can take.
    Make the answers as specific and helpful as they can be. Make the answers short and easy to read. Also have a hindi translation of the answer. The hindi should not be too complicated and should contain words only used in normal conversations.

    Answer the following question - '{query}'

    Some information about the farmer's field is given below -
    The farmer's field stage is {field}
    The current weather is {weather}
    Past diseases affecting the crop are {history}
    The soil type is {soil}
     """
def assistant_reply(prompt):
    client = Groq(
    api_key = ('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')
      )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )

    print(chat_completion.choices[0].message.content)

assistant_reply(prompt)
    
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    field1 = request.form.get("field")
    field2 = request.form.get("weather")
    field3 = request.form.get("history")
    field4 = request.form.get("soil")
    query = request.form.get("query")

    response = f"Processed Query: {query} with inputs {field1}, {field2}, {field3}, {field4}"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
