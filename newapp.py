from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("chat.html")
 
@app.route("/get", methods =["GET" ,"POST"])
def chat():
    if request.method == "POST":
        user_input = request.form["msg"]
        #Name of the field in html is msg

        bot_response = get_chat_response(user_input)
        return jsonify({"Yana": bot_response})
    
    else:
        return jsonify({"Error:"  "Invalid request method"})

def get_chat_response(text): 
    # Set up your OpenAI API credentials, authentication 
    openai.api_key = 'your open ai key'


    # Construct the conversation input for OpenAI GPT-3.5-turbo
    conversation = [
        {"role": "system", "content": "You are a friendly and helpful assistant that is ready to talk about mental health."},
        {"role": "user", "content": "Hi"}, 
    ]


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = conversation,
        temperature=0.5,
        max_tokens=120
    ) 
    
    print("Yana: ", response)

    # Extract and return the assistant's response from the API response
    return response['choices'][0]['message']['content']


if __name__ == '__main__':
    app.run(debug=True)

