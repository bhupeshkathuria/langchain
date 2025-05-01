from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#Create a AzureChatOpenAI model
llm = AzureChatOpenAI(
                azure_deployment="gpt-4o",  # or your deployment
                api_version="2024-12-01-preview",  # or your api version
            )

chat_history = [] #use a list to store messages

# Set an initial system message
system_message = SystemMessage("You are a helpful AI assistant")
chat_history.append(system_message) # Add system message to chat history


# Chat Loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query)) # Add user message to chat history

    # Get AI response using history
    result = llm.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response)) # Add AI message to chat history
    print(f"AI: {response}")

    print("Chat History:")
    print(chat_history) # Print chat history


messages= [
    SystemMessage("You are an expert in social media content strategy"),
    HumanMessage("What are some tips for creating engaging content on Instagram?")
]

result = llm.invoke(messages)

print(result.content)   