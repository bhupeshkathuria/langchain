from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#Create a ChatAnthropic model
llm = ChatAnthropic(
                model="claude-3-7-sonnet-20250219",
                temperature=0,
                max_tokens=1024,
                timeout=None,
                max_retries=2,
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