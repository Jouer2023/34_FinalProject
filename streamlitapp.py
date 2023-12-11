
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key= "your openai key")

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

def chat_with_bot(messages):
    # Get the user's message
    user_message = messages[-1]["content"]

    # Get the category of the response using a separate function
    response_category = get_response_category(user_message)

    # Append the category to the system message
    messages.append({"role": "assistant", "content": response_category})

    # Make a request to the OpenAI Chat API
    response = get_completion_from_messages(messages)

    # Extract and return the assistant's response from the API response
    return response

def get_response_category(user_message):
    # Define the categories offered by the chatbot
    categories_dict = {
        "Empathetic and understanding responses": {
            "keywords": ["empathy", "understanding"],
            "action": "Provide empathetic and supportive responses.",
        },
        "Active listening": {
            "keywords": ["listening", "engagement"],
            "action": "Actively listen to the user's concerns and engage in the conversation.",
        },
        "Resource provision": {
            "keywords": ["resources", "information"],
            "action": "Offer relevant resources and information to assist the user.",
        },
        "Daily positive affirmations": {
            "keywords": ["affirmations", "positivity"],
            "action": "Share daily positive affirmations to uplift the user's mood.",
        },
        "Constant improvement": {
            "keywords": ["improvement", "feedback"],
            "action": "Seek feedback for constant improvement and better user experience.",
        },
        "Off topic": {
            "keywords": ["off topic", "random"],
            "action": "Handle off-topic questions gracefully and guide the user back to the main topics.",
        }
    }

    # Construct a prompt that includes the categories and actions
    category_prompt = f"""Predict the category for the following user \ 
    message: '{user_message}'\nCategories: {', '.join(categories_dict.keys())}\nCategory:\
    return the category in the format, category:action"""
    category_response = get_completion(category_prompt)

    # Extract the predicted category from the model response    
    return category_response

def main():
    st.title("Yana Care")

    st.write("Hello! I'm Yana, your custom chatbot here to support you.")

    # Initialize the conversation with a system message
    messages = [{"role": "system", "content": "You are a friendly and helpful assistant ready to talk about mental health."}]

    # Get user input
    user_input = st.text_input("You:")

    # Appends the user's message to the conversation
    messages.append({"role": "user", "content": user_input})

    # Provides a response for the user and displays it
    if st.button("Send"):
        bot_response = chat_with_bot(messages)
        st.text_area("Yana:", value=bot_response)

if __name__ == "__main__":
    main()
