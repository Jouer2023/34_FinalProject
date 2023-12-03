# Imports the needed libraries
import openai
import os

# Set your OpenAI API key
openai.api_key = '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'


# Function to interact with the GPT-3.5 model
def chat_with_bot(messages):
    # Make a request to the OpenAI Chat API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=120
    )
    # Extract and return the assistant's response from the API response
    return response['choices'][0]['message']['content']



# Function to start the chat application
def start_chat():
    # Prints a welcome message
    print("Yana: Hello! How can I assist you today?")

    # Initialize the conversation with a system message
    messages = [
        {"role": "system", "content": "You are a friendly and helpful assistant."},
    ]

    # Condition to carry on with the message until the user says bye 
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Checks if the user wants to end the conversation
        if user_input.lower() == 'bye':
            print("Yana: Goodbye!")
            break

        #Checks if the user wants to clear context
        elif user_input.lower() == 'clear context':
            clear_context(messages)
            messages[:] = [{"role": "system", "content": "You are a friendly and helpful assistant."}] #Starts with the system message


        #Carries on with the chat if nothing
        else:
            messages.append({"role": "user", "content": user_input})
            bot_response = chat_with_bot(messages)
            print("Yana:", bot_response)

        # Appends the user's message to the conversation
        messages.append({"role": "user", "content": user_input})
        
        # Gets the assistant's response using the chat_with_bot function
        bot_response = chat_with_bot(messages)
        
        # Print the assistant's response
        print("Yana:", bot_response)



#Welcome message
print("Hi, I am Yana, a text-based AI assistant that will act as your supportive system to the end.")

#Starts the conversation by calling the function
start_chat()
