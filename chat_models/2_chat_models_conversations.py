from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

llm = ChatAnthropic(
                model="claude-3-7-sonnet-20250219",
                temperature=0,
                max_tokens=1024,
                timeout=None,
                max_retries=2,
            )
# Example of a conversation with multiple messages

messages= [
    SystemMessage("You are an expert in social media content strategy"),
    HumanMessage("What are some tips for creating engaging content on Instagram?")
]

result = llm.invoke(messages)

print(result.content)   