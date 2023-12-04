import openai

# Set your OpenAI API key
openai.api_key = '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'

# Define the purpose of your bot - it is small scale
# My bot serves as a mental health support and companionship system.

# Features to have
# Empathetic and understanding
# Active listener
# Resource provision
# Daily positive affirmations
# Safety and privacy
# Issuing a terms and conditions policy
# Constant improvement

# Conversational flow or training data
messages = [
    {"role": "system", "content": "You are a friendly and helpful assistant."},
    {"role": "user", "content": "I feel overwhelmed"},
    {"role": "assistant", "content": "I understand how you feel."},
    {"role": "user", "content": "You do?"},
    {"role": "assistant", "content": "Yeah, sometimes things become so hectic and I feel stuck in a loop, something of that sort. You?"},
    {"role": "user", "content": "I think mine is college life, it is stressing me way too much and I feel so behind."},
    {"role": "assistant", "content": "I get it."},
    {"role": "user", "content": "Got any suggestions to help."},
    {"role": "assistant", "content": "Yeah, a few. Seek assistance from time management doctors."},
    {"role": "user", "content": "Thanks, it was nice speaking to you Yana. Bye!"},
    {"role": "assistant", "content": "Same here, have a lovely day. Goodbye!"},
]


# Function to interact with the GPT-3.5 model for testing
def chat_with_bot(messages):
    # Make a request to the OpenAI Chat API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        temperature=0.5,
        max_tokens=120
    )
    # Extract and return the assistant's response from the API response
    return response['choices'][0]['message']['content']


# Function to start the chat application
def start_chat():
    # Prints a welcome message
    print("Yana: Hello, what's up?")

    # Initialize the conversation with a system message
    messages = [
        {"role": "system", "content": "You are a friendly and helpful assistant that is ready to talk about mental health."},
    ]

    # Condition to carry on with the message until the user says bye
    while True:
        # Get user input
        user_input = input("You: ")

        # Checks if the user wants to end the conversation
        if user_input.lower() == 'bye':
            print("Yana: Goodbye!")
            break

        # Checks if the user wants to clear context
        elif user_input.lower() == 'clear context':
            messages = clear_context()

        # Carries on with the chat if nothing
        else:
            # Appends the user's message to the conversation and asks for a friendly response
            messages.append({"role": "user", "content": user_input})
            messages.append({"role": "system", "content": "Please provide a friendly and empathetic response"})

            # Provides a response for the user and prints it out
            bot_response = chat_with_bot(messages)
            print("Yana:", bot_response)

        # Appends the user's message to the conversation
        messages.append({"role": "user", "content": user_input})

        # Gets the assistant's response using the chat_with_bot function
        bot_response = chat_with_bot(messages)

        # Print the assistant's response
        print("Yana:", bot_response)


# Train and fine-tune the model

# Welcome message
print("Hi, I am Yana, a text-based AI assistant that will act as your supportive system to the end.")


# Start the conversation by calling the function
start_chat()

# Function to clear context and start again
def clear_context():
    return [
        {"role": "system", "content": "You are a friendly and helpful assistant."},
    ]
